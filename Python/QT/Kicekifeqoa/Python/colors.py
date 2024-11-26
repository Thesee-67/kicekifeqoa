from PySide6.QtCore import QObject, Property

class Colors(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    @Property(str, constant=True)
    def couleur1(self):
        return "#4E598C"

    @Property(str, constant=True)
    def couleur2(self):
        return "#FFFFFF"

    @Property(str, constant=True)
    def couleur3(self):
        return "#F9C784"

    @Property(str, constant=True)
    def couleur4(self):
        return "#FCAF58"

    @Property(str, constant=True)
    def couleur5(self):
        return "#FF8C42"

    @Property(str, constant=True)
    def couleur6(self):
        return "#BC6C25"

    @Property(str, constant=True)
    def couleur7(self):
        return "#BCBCBC"
