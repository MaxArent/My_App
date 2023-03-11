from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.scatter import Scatter


class DogApp(Scatter, FloatLayout):
    def __init__(self, **kwargs):
        super(DogApp, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size = Window.size
        self.do_translation = False
        self.do_rotation = False
        self.do_scale = True
        self.scale_min = 1
        self.scale_max = 2
        self.scale = 1

        container = FloatLayout(size_hint=(None, None), size=(Window.width, Window.height),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        container.do_translation = False

        self.background = Image(source=r"Dog.jpg", allow_stretch=True,
                                keep_ratio=False, size_hint=(1, 1), size=(Window.width, Window.height),
                                pos_hint={'x': 0, 'y': 0})
        self.add_widget(self.background)
        self.background.auto_bring_to_front = False

        self.create_column1()
        self.create_column2()
        self.create_GridLayout()

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.scale = 1.0
            self.center = self.parent.center
            return True

        if touch.is_mouse_scrolling or (len(self._touches) == 1 and not self.collide_point(*touch.pos)):
            return False
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.is_double_tap:
            self.scale = 1.0
            self.center = self.parent.center
            return True
        return super().on_touch_up(touch)

    def on_transform_with_touch(self, touch):
        if self.scale > 1:
            self.do_translation = True
            self.do_rotation = False
        else:
            self.do_translation = False
            self.do_rotation = False
        super().on_transform_with_touch(touch)

    def create_column1(self):

        # Создаем BoxLayout для первого столбца
        column1 = BoxLayout(orientation='vertical', pos_hint={'center_x': .12, 'center_y': .75}, size_hint=(0.25, 0.45),
                            padding=40, spacing=20)
        self.add_widget(column1)

        # Создаем виджет Label с названием поля ввода
        label1 = Label(text='Вес при Рождении', size_hint=(1, 0.2), font_size=24, color=(0.3, 0.3, 0.3, 1), bold=True)
        column1.add_widget(label1)

        # Создаем поле пользовательского ввода в первом столбце
        self.input1 = TextInput(size_hint=(1, 0.6), font_size=24, background_normal='', background_color=(1, 1, 1, 1),
                                multiline=False, write_tab=False, halign='center')
        column1.add_widget(self.input1)

        # Создаем кнопку расчета в первом столбце
        button1 = Button(text='Рассчитать', pos_hint={'center_x': .5, 'center_y': 1}, size_hint=(0.5, 0.5),
                         font_size=24, background_normal='', background_color=(0, 0.7, 0.5, 1), color=(1, 1, 1, 1),
                         bold=True, on_press=self.result1)
        column1.add_widget(button1)

        # Создаем BoxLayout для поля вывода результата в первом столбце
        result1_layout = BoxLayout(orientation='vertical', pos_hint={'center_x': 0.5, 'center_y': 1})
        column1.add_widget(result1_layout)

        # Создаем виджет Label для поля вывода результата в первом столбце
        result1_label = Label(text='Вес Взрослой Собаки', size_hint=(1, 0.8), font_size=24, halign='center',
                              valign='middle', color=(0.3, 0.3, 0.3, 1), bold=True)

        result1_layout.add_widget(result1_label)

        # Создаем поле вывода результата в первом столбце
        self.result1_input = TextInput(size_hint=(1, 1), font_size=24, background_normal='',
                                       background_color=(1, 1, 1, 1), readonly=True, halign='center')
        result1_layout.add_widget(self.result1_input)

    def result1(self, instance):
        try:
            AdultBirthWeight = float(self.input1.text)
            if AdultBirthWeight <= 71:
                label_text = AdultBirthWeight * 12.78
            elif AdultBirthWeight > 71 and AdultBirthWeight <= 78:
                label_text = AdultBirthWeight * 14.55
            elif AdultBirthWeight > 78 and AdultBirthWeight <= 85:
                label_text = AdultBirthWeight * 16.02
            elif AdultBirthWeight > 85 and AdultBirthWeight <= 99:
                label_text = AdultBirthWeight * 16.05
            elif AdultBirthWeight > 99 and AdultBirthWeight <= 113:
                label_text = AdultBirthWeight * 16.07
            elif AdultBirthWeight > 113 and AdultBirthWeight <= 120:
                label_text = AdultBirthWeight * 17.02
            elif AdultBirthWeight > 120 and AdultBirthWeight <= 128:
                label_text = AdultBirthWeight * 17.73
            elif AdultBirthWeight > 128 and AdultBirthWeight <= 142:
                label_text = AdultBirthWeight * 17.58
            elif AdultBirthWeight > 142 and AdultBirthWeight <= 156:
                label_text = AdultBirthWeight * 17.46
            elif AdultBirthWeight > 156 and AdultBirthWeight <= 170:
                label_text = AdultBirthWeight * 17.64
            else:
                label_text = AdultBirthWeight * 17.60
            self.result1_input.text = str(round(label_text))
        except ValueError:
            self.result1_input.text = 'Введите только цифры!'

    def create_column2(self):

        # Создаем BoxLayout для второго столбца
        column2 = BoxLayout(orientation='vertical', pos_hint={'center_x': .4, 'center_y': .75}, size_hint=(0.25, 0.45),
                            padding=40, spacing=20)
        self.add_widget(column2)

        # Создаем виджет Label с названием поля ввода
        label2 = Label(text='Вес Взрослой Собаки', size_hint=(1, 0.2), font_size=24, color=(0.3, 0.3, 0.3, 1),
                       bold=True)
        column2.add_widget(label2)

        # Создаем поле пользовательского ввода во втором столбце
        self.input2 = TextInput(size_hint=(1, 0.6), font_size=24, background_normal='', background_color=(1, 1, 1, 1),
                                multiline=False, write_tab=False, halign='center')
        column2.add_widget(self.input2)

        # Создаем кнопку расчета во втором столбце
        button2 = Button(text='Рассчитать', pos_hint={'center_x': .5, 'center_y': 1}, size_hint=(0.5, 0.5),
                         font_size=24, background_normal='', background_color=(0, 0.7, 0.5, 1), color=(1, 1, 1, 1),
                         bold=True, on_press=self.result2)
        column2.add_widget(button2)

        # Создаем BoxLayout для поля вывода результата во втором столбце
        result2_layout = BoxLayout(orientation='vertical', pos_hint={'center_x': .5, 'center_y': 1})
        column2.add_widget(result2_layout)

        # Создаем виджет Label для поля вывода результата во втором столбце
        result2_label = Label(text='Класс Питомца', size_hint=(1, 0.8), font_size=24, halign='center', valign='middle',
                              color=(0.3, 0.3, 0.3, 1), bold=True)
        result2_layout.add_widget(result2_label)

        # Создаем поле вывода результата во втором столбце
        self.result2_input = TextInput(size_hint=(1, 1), font_size=24, background_normal='',
                                       background_color=(1, 1, 1, 1), readonly=True, halign='center')
        result2_layout.add_widget(self.result2_input)

    def result2(self, instance):
        try:
            dog_weight = float(self.input2.text)
            if dog_weight <= 1299:
                label_text = 'Tiny'
            elif dog_weight <= 1999:
                label_text = 'Small'
            elif dog_weight <= 2399:
                label_text = 'Medium'
            elif dog_weight <= 3000:
                label_text = 'Large'
            elif dog_weight <= 4000:
                label_text = 'Very Large'
            else:
                label_text = 'Это точно Чихуахуа?'
            self.result2_input.text = str(label_text)
        except ValueError:
            self.result2_input.text = 'Введите только цифры!'

    def create_GridLayout(self):

        # Создаем GridLayout для таблицы
        table = GridLayout(cols=7, pos_hint={'center_x': 0.40, 'center_y': 0.25}, size_hint=(0.80, 0.4), padding=5,
                           spacing=60)
        self.add_widget(table)

        # Создаем заголовки столбцов таблицы
        table.add_widget(
            Label(text='Вид корма', font_size=24, color=(0.3, 0.3, 0.3, 1), bold=True, text_size=(180, None),
                  halign='left'))
        table.add_widget(
            Label(text='Вес собаки 1 кг', font_size=24, color=(0.3, 0.3, 0.3, 1), bold=True, halign='left'))
        table.add_widget(
            Label(text='Вес собаки 1.5 кг', font_size=24, color=(0.3, 0.3, 0.3, 1), bold=True, halign='left'))
        table.add_widget(
            Label(text='Вес собаки 2 кг', font_size=24, color=(0.3, 0.3, 0.3, 1), bold=True, halign='left'))
        table.add_widget(
            Label(text='Вес собаки 2.5 кг', font_size=24, color=(0.3, 0.3, 0.3, 1), bold=True, halign='left'))
        table.add_widget(
            Label(text='Вес собаки 3 кг', font_size=24, color=(0.3, 0.3, 0.3, 1), bold=True, halign='left'))
        table.add_widget(
            Label(text='Вес собаки 3.5 кг', font_size=24, color=(0.3, 0.3, 0.3, 1), bold=True, halign='left'))

        # Создаем ячейки таблицы
        table.add_widget(
            Label(text='Сухой корм (гр)', font_size=24, color=(0.3, 0.3, 0.3, 1), text_size=(180, None), halign='left'))
        table.add_widget(Label(text='28', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='38', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='47', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='56', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='64', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='72', font_size=24, color=(0.3, 0.3, 0.3, 1)))

        table.add_widget(
            Label(text='Натуральный корм всего (гр):', font_size=24, color=(0.3, 0.3, 0.3, 1), text_size=(180, None),
                  halign='left'))
        table.add_widget(Label(text='65', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='80', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='90', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='105', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='105', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='120', font_size=24, color=(0.3, 0.3, 0.3, 1)))

        table.add_widget(
            Label(text='-мясо, рыба', font_size=24, color=(0.3, 0.3, 0.3, 1), text_size=(180, None), halign='left'))
        table.add_widget(Label(text='20', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='25', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='30', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='35', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='35', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='40', font_size=24, color=(0.3, 0.3, 0.3, 1)))

        table.add_widget(
            Label(text='-крупы', font_size=24, color=(0.3, 0.3, 0.3, 1), text_size=(180, None), halign='left'))
        table.add_widget(Label(text='10', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='15', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='15', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='20', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='20', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='20', font_size=24, color=(0.3, 0.3, 0.3, 1)))

        table.add_widget(
            Label(text='-овощи,фрукты', font_size=24, color=(0.3, 0.3, 0.3, 1), text_size=(180, None), halign='left'))
        table.add_widget(Label(text='20', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='25', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='30', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='35', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='35', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='40', font_size=24, color=(0.3, 0.3, 0.3, 1)))

        table.add_widget(
            Label(text='-кисломолочные продукты', font_size=24, color=(0.3, 0.3, 0.3, 1), text_size=(180, None),
                  halign='left'))
        table.add_widget(Label(text='15', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='15', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='15', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='15', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='15', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(Label(text='20', font_size=24, color=(0.3, 0.3, 0.3, 1)))
        table.add_widget(
            Label(text='Энергия 3920 ккал/кг', font_size=20, color=(0.3, 0.3, 0.3, 1), bold=True, halign='center'))

        pass


class MyApp(App):
    def build(self):
        return DogApp()


if __name__ == '__main__':
    MyApp().run()