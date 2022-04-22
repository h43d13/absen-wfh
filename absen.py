# dipakai untuk memanggil webdriver
from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# dipakai untuk menjeda
import time

cobain = time.asctime(time.localtime(time.time()))
print(cobain)
print(
    "Automatisasi Absen dp-wfh/skemaraja \ndengan Web Selenium Pyhon \nCreated By : h43d13"
)

# memilih web browser
browser = webdriver.Firefox()

# array nip
nip = [
    [3175022708970001, 0, "WFO"],  # HA
    [3201256301000004, 0, "WFO"],  # MIDP
    [3217015908930003, 0, "WFO"],  # MS
    [3201161811910002, "18111991", "WFO"],  # AS
    [3175011609900003, "pulsar200", "WFO"],  # SP
    [198508012003121002, 0, "WFO"],  # DSDS
    [198711022008121001, 0, "WFO"],  # NTH
    [198411102003121006, 0, "WFO"],  # H
    [198503222006041002, 0, "WFO"],  # DASW
    [198606222006041003, 0, "WFO"],  # GK
    #   ["197601132006041001",0,"WFH"],  S
    [197511272006041001, 0, "WFO"],  # GN
    #   ["198404252010122001",0,"WFO"],  TNP
    #   [198312022008121001, 0, "WFH"],  # CS
    [199007212010121004, 0, "WFO"],  # AA
    [197903022003121001, 0, "WFO"],  # AA
    [196404251986031002, 0, "WFO"],  # R
    [198302082003121003, 0, "WFO"],  # AW
    [198009282003121009, 0, "WFO"],  # S
    #   ["197410212003122001",0,"WFO"],  L X
    [197507072003121002, 0, "WFO"],  # EY
    [197902252003121001, 0, "WFO"],  # DH
    [197904202003121002, 0, "WFO"],  # W
    #   [197711142003121001, 0, "WFO"],  # S
    [197708132003121001, 0, "WFO"],  # AP
    [197508152006041002, "Ayrahayu", "WFO"],  # R
    [198110012003121002, "alie@781", "WFO"],  # AS
    [197601132006041001, "Januari1976", "WFO"],  # M
]


def skemaraja():
    #     masuk ke web absen
    try:
        browser.get("https://skemaraja.dephub.go.id")
    except NoSuchElementException:
        browser.quit()
        skemaraja()


def WFO():
    # opsi bila WFH
    browser.find_element_by_xpath(
        '//*[@id="theForm"]/div/p[3]/select/option[2]'
    ).click()
    print("Select WFO     [ berhasil ]")

    # opsi bila masuk Shift 1
    browser.find_element_by_xpath('//*[@id="shift_1"]').click()
    print("Select Shift 1 [ berhasil ]")
    # time.sleep(1)

    # opsi bila masuk Shift 2
    # browser.find_element_by_xpath('//*[@id="shift_2"]').click()


def WFH():
    # opsi bila WFO
    browser.find_element_by_xpath(
        '//*[@id="theForm"]/div/p[3]/select/option[1]'
    ).click()
    print("Select WFH     [ berhasil ]")
    # time.sleep(1)


def DL():
    # opsi bila DL
    browser.find_element_by_xpath(
        '//*[@id="theForm"]/div/p[3]/select/option[3]'
    ).click()
    print("Select DL      [ berhasil ]")
    # time.sleep(1)


# definisi absen
def absen(nip, pas, st):
    skemaraja()

    # input NIP
    browser.find_element_by_name("nip").send_keys(nip)
    print("Input NIP      [ berhasil ]")
    # time.sleep(1)

    # input pass
    browser.find_element_by_name("password").send_keys(pas)
    print("Input Pass     [ berhasil ]")
    # time.sleep(1)

    if st == "WFO":
        WFO()
    elif st == "WFH":
        WFH()
    elif st == "DL":
        DL()
    else:
        print("salah")

    # klik submit
    try:
        browser.find_element_by_id("btnSubmit").click()
        print("Login          [ berhasil ]")
    except NoSuchElementException:
        browser.refresh()
        print("Login          [ refresh  ]")
    # time.sleep(0.3)

    # testing add Exception by hadi
    try:
        browser.find_element_by_name("p1_suhu").send_keys("36.5")
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[1]/td[4]/input"
        ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[4]/input"
        ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[3]/td[4]/input"
        ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[4]/td[4]/input"
        ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[5]/td[4]/input"
        ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[6]/td[4]/input"
        ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[7]/td[4]/input"
        ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[8]/td[4]/input"
        ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[9]/td[4]/input"
        ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[3]/button"
        ).click()
        print("Submit 1       [ OPSI 2 ]")
    except NoSuchElementException:
        print("Submit 1       [ terlewat ]")

    # time.sleep(0.3)
    try:
        # browser.find_element_by_name("p1_suhu").send_keys("36.5")
        # browser.find_element_by_xpath(
        #     "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[1]/td[4]/input"
        # ).click()
        # browser.find_element_by_xpath(
        #     "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[4]/input"
        # ).click()
        # browser.find_element_by_xpath(
        #     "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[3]/td[4]/input"
        # ).click()
        # browser.find_element_by_xpath(
        #     "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[4]/td[4]/input"
        # ).click()
        # browser.find_element_by_xpath(
        #     "/html/body/div/di
        # v/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[5]/td[4]/input"
        # ).click()
        # browser.find_element_by_xpath(
        #     "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[6]/td[4]/input"
        # ).click()
        # browser.find_element_by_xpath(
        #     "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[7]/td[4]/input"
        # ).click()
        # browser.find_element_by_xpath(
        #     "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[8]/td[4]/input"
        # ).click()
        # browser.find_element_by_xpath(
        #     "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[9]/td[4]/input"
        # ).click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[3]/button"
        ).click()
        print("Submit 2       [ OPSI 1 ]")
    except NoSuchElementException:
        print("Submit 2       [ terlewat ]")
        # time.sleep(3)

    # browser.find_element_by_class_name("profile-username text-center").get_property()
    # keluar dari absen
    try:
        browser.get("https://skemaraja.dephub.go.id/logout")
        #    browser.quit()
        # try:
        #    browser.find_element_by_link_text("Check Out").click()
        print("Logout         [ berhasil ]")
    except NoSuchElementException:
        browser.quit()
        skemaraja()
        print("Logout         [ refresh  ]")
    # time.sleep(0.3)


# looping nip dan pass absen
for x in range(len(nip)):
    print("\nloop ke-", x + 1, nip[x][0])
    if nip[x][1] == 0:
        absen(nip[x][0], nip[x][0], nip[x][2])
    else:
        absen(nip[x][0], nip[x][1], nip[x][2])

browser.quit()
print("\nAutomatisasi Absen dengan Web Selenium Python... Selesai")
exit()
