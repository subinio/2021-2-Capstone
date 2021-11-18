(function($) {
    "use strict"


    //todo list
    $(".tdl-new").on('keypress', function(e) {

        var code = (e.keyCode ? e.keyCode : e.which);

        if (code == 13) {

            var v = $(this).val();

            var s = v.replace(/ +?/g, '');

            if (s == "") {

                return false;

            } else {

                $(".tdl-content ul").append("<li><label><input type='checkbox'><i></i><span>" + v + "</span><a href='#' class='ti-trash'></a></label></li>");

                $(this).val("");

            }

        }

    });





    $(".tdl-content a").on("click", function() {

        var _li = $(this).parent().parent("li");

        _li.addClass("remove").stop().delay(100).slideUp("fast", function() {

            _li.remove();

        });

        return false;

    });



    // for dynamically created a tags

    $(".tdl-content").on('click', "a", function() {

        var _li = $(this).parent().parent("li");

        _li.addClass("remove").stop().delay(100).slideUp("fast", function() {

            _li.remove();

        });

        return false;

    });








})(jQuery);


(function($) {
    "use strict"


     // LINE CHART
      // Morris bar chart
 Morris.Bar({
    element: 'morris-bar-chart',
    data: [{
        y: '2021-06',
        a: 50,
        b: 40,
    }, {
        y: '2021-07',
        a: 75,
        b: 90,
    }, {
        y: '2021-08',
        a: 80,
        b: 80,
    }, {
        y: '2021-09',
        a: 75,
        b: 65,
    }, {
        y: '2021-10',
        a: 100,
        b: 60,
    }, {
        y: '2021-11',
        a: 75,
        b: 65,
    }, {
        y: '2021-12',
        a: 100,
        b: 90,
    }],
    xkey: 'y',
    ykeys: ['a', 'b', 'c'],
    labels: ['입소자', '퇴소자', 'C'],
    barColors: ['#FC6C8E', '#7571f9'],
    hideHover: 'auto',
    gridLineColor: 'transparent',
    resize: true
});
})(jQuery);




(function($) {
  "use strict"


   // LINE CHART
    // Morris bar chart
Morris.Bar({
  element: 'morris-bar-chart2',
  data: [{
      y: '2021-06',
      a: 100,
      b: 90,
  }, {
      y: '2021-07',
      a: 75,
      b: 65,
  }, {
      y: '2021-08',
      a: 50,
      b: 40,
  }, {
      y: '2021-09',
      a: 75,
      b: 65,
  }, {
      y: '2021-10',
      a: 50,
      b: 40,
  }, {
      y: '2021-11',
      a: 75,
      b: 65,
  }, {
      y: '2021-12',
      a: 100,
      b: 90,
  }],
  xkey: 'y',
  ykeys: ['a', 'b', 'c'],
  labels: ['확진자', '완치자', 'C'],
  barColors: ['#4d7cff', '#fd7e14'],
  hideHover: 'auto',
  gridLineColor: 'transparent',
  resize: true
});
})(jQuery);





(function($) {
    "use strict"


    $('#todo_list').slimscroll({
        position: "right",
        size: "5px",
        height: "250px",
        color: "transparent"
    });

    $('#activity').slimscroll({
        position: "right",
        size: "5px",
        height: "390px",
        color: "transparent"
    });





})(jQuery);



(function($) {
    "use strict"

    let ctx = document.getElementById("chart_widget_2");
    ctx.height = 280;
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["11월 1주차", "11월 2주차", "11월 3주차", "11월 4주차", "11월 5주차", "12월 1주차"],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [{
                data: [12, 15, 57, 12, 85, 10],
                label: "긍정적 감정",
                backgroundColor: 'rgba(32, 162, 219, 0.5)',
                borderColor: '#00A9A2',
                borderWidth: 0.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: '#00A9A2',
            }, {
                label: "중립",
                data: [14, 30, 5, 53, 15, 55],
                backgroundColor: '#f9d423',
                opacity:0.8,
                borderColor: '#f9d423',
                borderWidth: 0.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: '#f9d423',
            }, {
              label: "부정적 감정",
              data: [10, 44, 33, 60, 4, 77],
              backgroundColor: 'rgba(250, 58, 14, 0.5)',
              borderColor: '#fa3636',
              borderWidth: 0.5,
              pointStyle: 'circle',
              pointRadius: 5,
              pointBorderColor: 'transparent',
              pointBackgroundColor: '#fa3636',
            }]
        },
        options: {
            responsive: !0,
            maintainAspectRatio: false,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
            },
            legend: {
                display: false,
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },


            },
            scales: {
                xAxes: [{
                    display: false,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Month'
                    }
                }],
                yAxes: [{
                    display: false,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            },
            title: {
                display: false,
            }
        }
    });
})(jQuery);

(function($) {
    "use strict"

    let ctx = document.getElementById("chart_widget_3");
    ctx.height = 130;
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [{
                data: [0, 15, 57, 12, 85, 10],
                label: "iPhone X",
                backgroundColor: 'transparent',
                borderColor: '#847DFA',
                borderWidth: 2,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: '#847DFA',
                pointBackgroundColor: '#fff',
            }]
        },
        options: {
            responsive: !0,
            maintainAspectRatio: true,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#fff',
                bodyFontColor: '#fff',
                backgroundColor: '#000',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
            },
            legend: {
                display: false,
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },


            },
            scales: {
                xAxes: [{
                    display: false,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Month'
                    }
                }],
                yAxes: [{
                    display: false,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            },
            title: {
                display: false,
            }
        }
    });


    


})(jQuery);



/*******************
Chart Chartist
*******************/
(function($) {
    "use strict"


    new Chartist.Line("#chart_widget_3", {
        labels: ["1", "2", "3", "4", "5", "6", "7", "8"],
        series: [
            [4, 5, 1.5, 6, 7, 5.5, 5.8, 4.6]
        ]
    }, {
        low: 0,
        showArea: !1,
        showPoint: !0,
        showLine: !0,
        fullWidth: !0,
        lineSmooth: !1,
        chartPadding: {
            top: 4,
            right: 4,
            bottom: -20,
            left: 4
        },
        axisX: {
            showLabel: !1,
            showGrid: !1,
            offset: 0
        },
        axisY: {
            showLabel: !1,
            showGrid: !1,
            offset: 0
        }
    });


    new Chartist.Pie("#chart_widget_3_1", {
        series: [35, 65]
    }, {
        donut: !0,
        donutWidth: 10,
        startAngle: 0,
        showLabel: !1
    });

})(jQuery);




/*******************
Pignose Calender
*******************/
(function ($) {
    "use strict";

    $(".year-calendar").pignoseCalendar({
        theme: "blue"
    }), $("input.calendar").pignoseCalendar({
        format: "YYYY-MM-DD"
    });

})(jQuery);