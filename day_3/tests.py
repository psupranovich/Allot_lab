
from pages.client_side_delay import ClientSideDelay
from pages.load_delay import LoadDelay
from pages.ajax_data import AjaxData
from pages.click import BadClick


link = "http://uitestingplayground.com/"

#
# def test_user_can_load_delay_page(browser):
#     page = LoadDelay(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     load_delay_page = page.go_to_load_delay_page()
#     load_delay_page.should_be_load_delay_page()# выполняем метод страницы — переход


# def test_user_can_load_ajax_data_and_see_element(browser):
#     page = AjaxData(browser, link)
#     page.open()
#     ajax_data_page = page.go_to_ajax_data_page()
#     new_page = ajax_data_page.should_be_ajax_button_on_ajax_data_page()
#     new_page.ajax_data_element_appear()



# def test_user_can_load_cliene_side_data_and_see_element(browser):
#     page = ClientSideDelay(browser, link)
#     page.open()
#     client_side_page = page.go_to_client_side_page()
#     new_page = client_side_page.should_be_client_side_page()
#     new_page.client_side_page_element_appear()


def test_uset_can_cLick_on_bad_button(browser):
    page = BadClick(browser, link)
    page.open()
    click_page = page.go_to_cLick_page()
    click_page.should_be_cLick_button()







