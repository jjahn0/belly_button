function buildPlot() {
    /* data route */
  var url = "/api/piePlot";
  Plotly.d3.json(url, function(error, response) {

    console.log(response);

    var data = response;

    // var data = [{
    //   type: 'pie',
    //   title: "BB Pie",
    //   values: [18096.0, 10078.0, 5876.0, 4295.0, 4244.0, 4017.0, 3875.0, 3012.0, 2160.0, 2049.0],
    //   labels: [1795, 922, 944, 2419, 1167, 2859, 2539, 2722, 482, 728]
    // }];

    var layout = {
      title: "BB pie chart",
      height: 200,
      width: 200
    };

    Plotly.newPlot("plot", data, layout);
  });
}

buildPlot();
