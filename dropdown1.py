#MULTI-SELECT DROPDOWN
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://demoqa.com/select-menu")
multi_select_element = driver.find_element(By.ID,"cars")
multi_select = Select(multi_select_element)

multi_select.select_by_visible_text("Volvo")
multi_select.deselect_by_visible_text("Volvo")

multi_select.select_by_index(1)
multi_select.select_by_value("audi")

all_selected_opt_list = multi_select.all_selected_options
for opt in all_selected_opt_list:
    print(opt.text)

multi_select.deselect_by_index(0)
multi_select.deselect_by_value("audi")
multi_select.deselect_all()