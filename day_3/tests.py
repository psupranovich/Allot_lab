from .pages.load_delay import LoadDelay


link = "http://uitestingplayground.com/"

def test_guest_can_go_to_load_delay_page(browser):
    page = LoadDelay(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    load_delay_page = page.go_to_load_delay_page()
    load_delay_page.should_be_load_delay_page()# выполняем метод страницы — переход






