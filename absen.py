# dipakai untuk memanggi webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# dipakai untuk menjeda
import time
cobain = time.asctime(time.localtime(time.time()))
print(cobain)
print("Automatisasi Absen dp-wfh/skemaraja \ndengan Web Selenium Pyhon \nCreated By : h43d13")

# memilih web browser
browser = webdriver.Firefox()

# array nip
nip = ["3175022708970001", "3201256301000004", "3217015908930003", "198411102003121006",
       "198503222006041002", "198606222006041003", "196308021990111001", "197511272006041001",
       "198404252010122001", "198312022008121001", "199007212010121004", "197903022003121001",
       "196404251986031002", "198302082003121003", "198009282003121009", "197410212003122001",
       "197507072003121002", "197902252003121001", "197904202003121002", "197711142003121001",
       "197708132003121001", "198508012003121002",
       "197508152006041002", "198110012003121002", "3201161811910002"]
# array pass
pas = ["Ayrahayu", "alie@781", "18111991"]


def skemaraja():
    # masuk ke web absen
    try:
        browser.get('https://dp-wfh.dephub.go.id')
    except NoSuchElementException:
        browser.quit()
        skemaraja()

# definisi absen


def absen(nip, pas):
    skemaraja()

    # input NIP
    browser.find_element_by_name('nip').send_keys(nip)
    print("Input NIP      [ berhasil ]")
    # time.sleep(1)

    # input pass
    browser.find_element_by_name('password').send_keys(pas)
    print("Input Pass     [ berhasil ]")
    # time.sleep(1)

    # opsi bila WFH
    # browser.find_element_by_xpath('//*[@id="theForm"]/div/p[3]/select/option[1]').click()

    # opsi bila WFO
    browser.find_element_by_xpath(
        '//*[@id="theForm"]/div/p[3]/select/option[2]').click()
    print("Select WFO     [ berhasil ]")
    # time.sleep(1)

    # opsi bila masuk Shift 1
    browser.find_element_by_xpath('//*[@id="shift_1"]').click()
    print("Select Shift 1 [ berhasil ]")
    # time.sleep(1)

    # opsi bila masuk Shift 2
    # browser.find_element_by_xpath('//*[@id="shift_2"]').click()

    # klik submit
    try:
        browser.find_element_by_id('btnSubmit').click()
        print("Login          [ berhasil ]")
    except NoSuchElementException:
        browser.refresh()
        print("Login          [ refresh  ]")
    # time.sleep(0.3)

    # testing add Exception by hadi
    try:
        browser.find_element_by_xpath(
            '/html/body/div/div/div[2]/div/div[2]/div/form/div/div[3]/button').click()
        print("Submit 1       [ berhasil ]")
    except NoSuchElementException:
        print("Submit 1       [ terlewat ]")
    time.sleep(0.3)
    try:
        browser.find_element_by_xpath(
            '/html/body/div/div/div[2]/div/div[2]/div/form/div/div[3]/button').click()
        print("Submit 2       [ berhasil ]")
    except NoSuchElementException:
        print("Submit 2       [ terlewat ]")
    time.sleep(0.3)

    # keluar dari absen
    try:
        browser.get('https://dp-wfh.dephub.go.id/logout')
    #    browser.quit()
    # try:
    #    browser.find_element_by_link_text("Check Out").click()
        print("Logout         [ berhasil ]")
    except NoSuchElementException:
        browser.quit()
        skemaraja()
        print("Logout         [ refresh  ]")
    time.sleep(0.3)


# looping nip dan pass absen
for x in range(22):
    print("\nloop ke-", x+1)
    absen(nip[x], nip[x])
for x in range(3):
    print("\nloop ke-", x+23)
    absen(nip[x+22], pas[x])
else:
    browser.quit()
    print("\nAutomatisasi Absen dengan Web Selenium Python... Selesai")
exit()
