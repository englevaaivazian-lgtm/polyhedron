import unittest
import os
from shadow.polyedr import Polyedr


class TestPolyedrCoverage(unittest.TestCase):

    def get_ans(self, name):
        # Путь к файлу в папке data
        path = os.path.join("data", f"{name}.geom")
        p = Polyedr(path)
        # Нам нужно вызвать расчет теней.
        # В твоем коде это происходит внутри draw()
        # Можно передать объект-заглушку вместо tk

        class StubTK:
            def clean(self): pass
            def draw_line(self, p, q): pass

        p.draw(StubTK())
        # Возвращаем результат деленный на 2, как в твоем run_shadow.py
        return p.lenght_shadow() / 2.0

   
    def test_polyedr_1(self):
        """Частичное перекрытие, центр внутри сферы."""
        ans = self.get_ans("Polyedr_test1")
        self.assertEqual(ans, 8.0)

    def test_polyedr_2(self):
        """Заслонка смещена, перекрытия нет или оно вне сферы."""
        ans = self.get_ans("Polyedr_test2")
        self.assertEqual(ans, 0.0)

    def test_polyedr_3(self):
        """Большая заслонка, полное или значительное перекрытие."""
        ans = self.get_ans("Polyedr_test3")
        self.assertEqual(ans, 8.0)

    def test_polyedr_4(self):
        """Объекты далеко, центры ребер вне сферы."""
        ans = self.get_ans("Polyedr_test4")
        self.assertEqual(ans, 0.0)

    def test_polyedr_5(self):
        """Смещение по Y и Z, проверка точности расчета центра."""
        ans = self.get_ans("Polyedr_test5")
        self.assertEqual(ans, 2.0)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
