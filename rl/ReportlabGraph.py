from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing

d = Drawing(400, 200)
datos = [(13, 5, 14, 31, 24, 42, 7, 10), (1, 3, 6, 6, 15, 27, 31)]
gbarra = VerticalBarChart()
gbarra.x = 50
gbarra.y = 50
gbarra.height = 125
gbarra.width = 300
gbarra.data = datos
gbarra.valueAxis._valueMin = 0
gbarra.valueAxis._valueMax = 50
gbarra.valueAxis._valueStep = 10
gbarra.categoryAxis.labels.boxAnchor = 'ne'
gbarra.categoryAxis.labels.dx = 8
gbarra.categoryAxis.labels.dy = -2
gbarra.categoryAxis.labels.angle = 30
gbarra.categoryAxis.labels.categoryNames = []
