"""
My first application
"""
import ppb


class hellopursuedpybear(ppb.BaseScene):
    def __init__(self, **props):
        super().__init__(**props)

        self.add(ppb.Sprite(
            image=ppb.Image('hellopursuedpybear/resources/hellopursuedpybear.png'),
        ))


def main():
    ppb.run(
        starting_scene=hellopursuedpybear,
        title='hellopursuedpybear',
    )
