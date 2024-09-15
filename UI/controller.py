import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        years = self._model.getAllYears()
        shapes = self._model.getAllShapes()

        for a in years:
            self._view.ddyear.options.append(ft.dropdown.Option(a))
        for s in shapes:
            self._view.ddshape.options.append(ft.dropdown.Option(s))

        self._view.update_page()

    def handle_graph(self, e):
        s = self._view.ddshape.value
        y = self._view.ddyear.value
        self._model.buildGraph(s, y)
        n = self._model.getNodes()
        e = self._model.getEdges()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vertici: {n}, numero archi: {e}"))

        listaV = self._model.getWeight()
        for v, tot in listaV:
            self._view.txt_result.controls.append(ft.Text(f"Nodo: {v}, somma pesi su archi = {tot}"))


        self._view.update_page()



    def handle_path(self, e):
        pass
