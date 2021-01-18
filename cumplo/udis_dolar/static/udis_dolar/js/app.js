function obtenerInformacion() {
    var data = $("#consultarInfo").serialize();

    $.ajax({
        type:"POST",
        url: "index",
        data: data,
        success: function(data)
        {
            data.data.tabla = "resultadosUdis";
            data.data.datos = "datos_udis";
            data.data.elemento = "#paginationUdis";
            datos = data.data;
            datosValoresUdis = data.data.valores_udis;
            pagination(datos, datosValoresUdis);
            data.data.tabla = "resultadosTipoCambio";
            data.data.datos = "datos_tipo_cambio";
            data.data.elemento = "#paginationTipoCambio";
            datos = data.data;
            datosValoresCambios = data.data.valores_cambios;
            pagination(datos, datosValoresCambios);
        }
    })
}

function pagination(data, datos) {
    var container = $(data.elemento);
    container.pagination({
        dataSource: data,
        locator: data.datos,
        totalNumber: 50,
        pageSize: 10,
        showPageNumbers: true,
        showPrevious: true,
        showNext: true,
        showNavigator: false,
        showFirstOnEllipsisShow: true,
        showLastOnEllipsisShow: true,
        ajax: {
            beforeSend: function() {
            container.prev().html('Cargando datos ...');
            }
        },
        callback: function(response, pagination) {
            if (data.datos == "datos_udis") {
                descripcion = "Valor UDIS";
            } else if (data.datos == "datos_tipo_cambio") {
                descripcion = "Valor Pesos por Dólar"
            }

            var dataHtml = `<table id="${data.tabla}">
                                <tr>
                                    <th>Fecha</th>
                                    <th>${descripcion}</th>
                                    <th>Valor mínimo</th>
                                    <th>Valor máximo</th>
                                    <th>Valor promedio</th>
                                </tr>`;

            $.each(response, function (index, item) {
                dataHtml += `<tr>
                                <td>${item.fecha}</td>
                                <td>${item.dato}</td>`;
            });

            dataHtml += `<td>${datos.minimo}</td>
                        <td>${datos.maximo}</td>
                        <td>${datos.promedio}</td>
                        </tr>
                        </table>`;

            container.prev().html(dataHtml);
        }
    });
}

$(function() {
    $("#resultadosUdis").hide();
    $("#resultadosTipoCambio").hide();

    $("#consultar").on("click", function() {
        var fechaInicial = $("#fechaInicial").val();
        var fechaFinal = $("#fechaFinal").val();
        if (fechaInicial != "" && fechaFinal != "") {
            obtenerInformacion();
            $('.alert').attr("hidden", "hidden");
            $("#resultadosUdis").removeAttr("hidden");
            $("#resultadosUdis").show();
            $("#resultadosTipoCambio").removeAttr("hidden");
            $("#resultadosTipoCambio").show();
        } else {
            $('.alert').removeAttr("hidden");
        }
    });
});