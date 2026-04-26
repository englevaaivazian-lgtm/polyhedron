#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in [
        "Polyedr_test1",
        "Polyedr_test2",
        "Polyedr_test3",
        "Polyedr_test4",
        "Polyedr_test5",
        "ccc",
        "cube",
        "box",
        "king",
            "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        p = Polyedr(f"data/{name}.geom")
        start_time = time()
        p.draw(tk)
        delta_time = time() - start_time

        ans = p.lenght_shadow() / 2.0

        print(f"Сумма длин невидимых частей: {ans}")

        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")


except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
