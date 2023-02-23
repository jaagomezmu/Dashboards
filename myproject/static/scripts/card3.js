Highcharts.chart('container-pie', {
    chart: {

        height:150,
        width:505,

        type: 'pie'
    },
    title: {
        text: 'PARTICIPACIÓN',
        align: 'center'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
        pie: {
            size: '30%',
            allowPointSelect: true,
            
            dataLabels: {
                enabled: true,
                format: '{point.name}: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Participación',
        colorByPoint: true,
        data: objToArray(pie)
    }]
});
