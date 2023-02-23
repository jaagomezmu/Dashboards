var card2_motivo = card2['MOTIVO_RETIRO']
var card2_año = card2['AÑOS_EN_LA_EMPRESA']

card2_año = card2_año.map(function(each_element){
    return Number(each_element.toFixed(2));
});

$('#container-card2').highcharts({
    chart: {
        type: 'column',
        height:340
    },
    title: {
        text: 'MOTIVO DE RETIRO vs. PROMEDIO DE AÑOS EN LA EMPRESA',
    },
    xAxis: {
        tickWidth: 0,
        categories: card2_motivo
    },
    yAxis: {
        title: {
            text: 'PROMEDIO AÑOS EN LA EMPRESA',
        },
    },
    legend: {
        enabled: false,
    },
    credits: {
        enabled: false
    },
    tooltip: {
        valuePrefix: '',
    },
    plotOptions: {
        column: {
            borderRadius: 0,
            pointPadding: 0,
            groupPadding: 0.05
        }
    },
    series: [{
        name: 'Promedio de años en la empresa',
        color: {
            linearGradient: {
              x1: 0,
              x2: 0,
              y1: 0,
              y2: 1
            },
            stops: [
              [0, '#FF0000'],
              [1, '#ff8800']
            ]},
        data: card2_año
    }]
});