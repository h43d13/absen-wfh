# dipakai untuk memanggi webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# dipakai untuk menjeda
import time
# memilih web browser
browser = webdriver.Firefox()
# masuk ke web absen
browser.get('https://skemaraja.dephub.go.id')
# array nip
nip = ["3175022708970001", "3201256301000004", "3217015908930003", "198411102003121006",
       "198503222006041002", "198606222006041003", "196308021990111001", "197511272006041001",
       "198404252010122001", "198312022008121001", "199007212010121004", "197903022003121001",
       "196404251986031002", "198302082003121003", "198009282003121009", "197410212003122001",
       "197507072003121002", "197902252003121001", "197904202003121002", "197508152006041002",
       "198110012003121002", "3201161811910002"]
# array pas
pas = ["Ayrahayu", "alie@781", "18111991"]

# definisi absen


def absen(nip, pas):
    # input NIP
    browser.find_element_by_name('nip').send_keys(nip)
    # input pass
    browser.find_element_by_name('password').send_keys(pas)
    # opsi bila WFH
    # browser.find_element_by_xpath('//*[@id="theForm"]/div/p[3]/select/option[1]').click()
    # opsi bila WFO
    browser.find_element_by_xpath(
        '//*[@id="theForm"]/div/p[3]/select/option[2]').click()
    # opsi bila masuk Shift 1
    browser.find_element_by_xpath('//*[@id="shift_1"]').click()
    # opsi bila masuk Shift 2
    # browser.find_element_by_xpath('//*[@id="shift_2"]').click()
    # klik submit
    browser.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    
    # testing by hadi
    time.sleep(2)
    # keluar dari absen
    browser.get('https://dp-wfh.dephub.go.id/logout')
    #try:
        # klik submit data corona
    #    WebDriverWait(browser, 1).until(browser.find_element_by_xpath(
    #    '/html/body/div/div/div[2]/div/div[2]/div/form/div/div[3]/button').click())
    #finally:
        
# looping nip dan pass absen
for x in range(19):
    absen(nip[x], nip[x])
for x in range(3):
    absen(nip[x+19], pas[x])
else:
    browser.quit()
exit()