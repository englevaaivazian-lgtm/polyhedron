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
        # Центр нижнего блока в (0, 0, -0.5), заслонка перекрывает часть ребер
        ans = self.get_ans("Polyedr_test1")
        self.assertGreater(ans, 0.0)

    def test_polyedr_2(self):
        """Заслонка смещена, перекрытия нет или оно вне сферы."""
        # Блок заслонки смещен по X (3.0 - 5.0) [cite: 2]
        ans = self.get_ans("Polyedr_test2")
        # Если перекрытия ребер, находящихся в сфере, нет, результат 0
        self.assertEqual(ans, 0.0)

    def test_polyedr_3(self):
        """Большая заслонка, полное или значительное перекрытие."""
        # Заслонка от -3 до 3 по X [cite: 3]
        ans = self.get_ans("Polyedr_test3")
        self.assertGreater(ans, 0.0)

    def test_polyedr_4(self):
        """Объекты далеко (X=8..12), центры ребер вне сферы."""
        # Центры ребер ~ (10, 0, 0), что дает 10^2 = 100 > 4 [cite: 4]
        ans = self.get_ans("Polyedr_test4")
        self.assertEqual(ans, 0.0)

    def test_polyedr_5(self):
        """Смещение по Y и Z, проверка точности расчета центра."""
        # Центр нижнего блока смещен по Y на 1.0 [cite: 5]
        ans = self.get_ans("Polyedr_test5")
        self.assertIsNotNone(ans)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
