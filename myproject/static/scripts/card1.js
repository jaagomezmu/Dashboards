var card1_motivo = card1['MOTIVO_RETIRO']
var card1_salario = card1['TOTAL_SALARIO']

card1_salario = card1_salario.map(function(each_element){
    return Number(each_element.toFixed(2));
});

Highcharts.chart('container-card1', {
    chart: {
        width: 1025,
        height:150,
        type: 'line'
    },
    xAxis: {
      categories: card1_motivo,
    },
    yAxis: {
        title: {
            text: 'SALARIO TOTAL PROMEDIO',

        }
    },
    series: [{
      data: card1_salario,
      name: 'Salario total promedio',
      showInLegend: false,
      color: 'red'
    }],
    title: {
        text: 'MOTIVO DE RETIRO vs.SALARIO TOTAL PROMEDIO',
        align: 'center'
    },
});

