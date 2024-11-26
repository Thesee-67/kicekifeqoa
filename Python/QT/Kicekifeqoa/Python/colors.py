from PySide6.QtCore import QObject, Property

class Colors(QObject):
    def __init__(self, parent=None, style=1):
        super().__init__(parent)
        self.style = style

    @Property(str, constant=True)
    def couleur1(self):
        if self.style == 1:
            return "#4E598C"  # Fond bleu
        elif self.style == 2:
            return "#062B16"  # Vert
        elif self.style == 3:
            return "#9B5DE5"  # Violet

    @Property(str, constant=True)
    def couleur2(self):
        if self.style == 1:
            return "#FFFFFF"  # Blanc
        elif self.style == 2:
            return "#FFFFFF"  # Vert clair
        elif self.style == 3:
            return "#FFFFFF"  # Jaune vif

    @Property(str, constant=True)
    def couleur3(self):
        if self.style == 1:
            return "#F9C784"  # Orange clair
        elif self.style == 2:
            return "#52B788"  # Vert moyen
        elif self.style == 3:
            return "#F15BB5"  # Rose vif

    @Property(str, constant=True)
    def couleur4(self):
        if self.style == 1:
            return "#FCAF58"  # Orange
        elif self.style == 2:
            return "#40916C"  # Vert foncé
        elif self.style == 3:
            return "#00BBF9"  # Bleu clair

    @Property(str, constant=True)
    def couleur5(self):
        if self.style == 1:
            return "#FF8C42"  # Orange vif
        elif self.style == 2:
            return "#1B4332"  # Vert olive foncé
        elif self.style == 3:
            return "#3A0CA3"  # Violet foncé

    @Property(str, constant=True)
    def couleur6(self):
        if self.style == 1:
            return "#BC6C25"  # Marron
        elif self.style == 2:
            return "#74C69D"  # Vert pastel
        elif self.style == 3:
            return "#7209B7"  # Violet profond

    @Property(str, constant=True)
    def couleur7(self):
        if self.style == 1:
            return "#BCBCBC"  # Gris
        elif self.style == 2:
            return "#D8F3DC"  # Vert pâle
        elif self.style == 3:
            return "#F72585"  # Rose foncé