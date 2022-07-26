# dipakai untuk memanggil webdriver
from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from tabulate import tabulate as t

# dipakai untuk menjeda
import numpy as np
import threading
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
    [3175022708970001, 0, "DL"],  # HA
]
tabel = [["nama","Jabatan","Status","Unit Kantor", "Unit Kerja", "Sub Bagian"]]
cabel = tabel.copy()

def skemaraja():
    #     masuk ke web absen
    try:
        browser.get("https://skemaraja.dephub.go.id")
    except NoSuchElementException:
        browser.quit()
        skemaraja()

def WFO():
    # opsi bila WFO
    browser.find_element(By.XPATH,
        '//*[@id="theForm"]/div/p[3]/select/option[3]'
    ).click()
    print("Select WFO     [ berhasil ]")
    # time.sleep(1)

    # opsi bila masuk Shift 2
    # browser.find_element(By.XPATH,'//*[@id="shift_2"]').click()
    
    # opsi bila masuk Shift 1
    browser.find_element(By.XPATH, '//*[@id="shift_1"]').click()
    print("Select Shift 1 [ berhasil ]")

def WFH():
    # opsi bila WFH
    browser.find_element(By.XPATH,
        '//*[@id="theForm"]/div/p[3]/select/option[2]'
    ).click()
    print("Select WFH     [ berhasil ]")

def DL():
    # opsi bila DL
    browser.find_element(By.XPATH,
        '//*[@id="theForm"]/div/p[3]/select/option[4]'
    ).click()
    print("Select DL      [ berhasil ]")

def resiko():
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[3]/button"
    ).click()
    print("Form Resiko    [ berhasil ]")

def gejala():
    #   print(browser.find_element(By.CLASS_NAME, "brand-image").text)
    #   browser.execute_script("document.body.style.zoom='50%'")
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    browser.find_element(By.NAME, "p1_suhu").send_keys("36.5")
    browser.find_element(By.XPATH, 
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[1]/td[4]/input"
    ).click()
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[2]/td[4]/input"
    ).click()
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[3]/td[4]/input"
    ).click()
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[4]/td[4]/input"
    ).click()
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[5]/td[4]/input"
    ).click()
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[6]/td[4]/input"
    ).click()
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[7]/td[4]/input"
    ).click()
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[8]/td[4]/input"
    ).click()
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[2]/div/div/table/tbody/tr[9]/td[4]/input"
    ).click()
    #time.sleep(1)
    browser.find_element(By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[3]/button"
    ).click()
    print("Form Gejala    [ berhasil ]")

def info(tabel):
    nama = browser.find_element(By.CSS_SELECTOR, ".profile-username").text
    fung = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div/p").text
    unit = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div/ul/li[1]/div/div[2]").text
    kntr = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div/ul/li[2]/div/div[2]").text
    sktr = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div/ul/li[3]/div/div[2]").text
    stat = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div/ul/li[4]/div/div[2]").text
    kondisi = [["nama","Jabatan","Status","Unit Kantor", "Unit Kerja", "Sub Bagian"],[nama,fung,stat,unit,kntr,sktr]]
    tabel.append([nama,fung,stat,unit,kntr,sktr])

    print("report:")
    print(t(kondisi, headers="firstrow", tablefmt="psql"))

def login():
    info(tabel)
    #`keluar dari absen
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

# definisi absen
def absen(nip, pas, st):
    skemaraja()

    # input NIP
    browser.find_element(By.NAME, "nip").send_keys(nip)
    #browser.find_element_by_name("nip").send_keys(nip)
    print("Input NIP      [ berhasil ]")
    # time.sleep(1)

    # input pass
    browser.find_element(By.NAME, "password").send_keys(pas)
    #browser.find_element_by_name("password").send_keys(pas)
    print("Input Pass     [ berhasil ]")
    # time.sleep(1)


    if st == "WFO":
        WFO()
    if st == "WFH":
        WFH()
    if st == "DL":
        DL()
    else:
        print("salah")

    # klik submit
    try:
        browser.find_element(By.ID, "btnSubmit").click()
        #browser.find_element_by_id("btnSubmit").click()
        print("Login          [ berhasil ]")
    except NoSuchElementException:
        browser.refresh()
        print("Login          [ refresh  ]")
    # time.sleep(0.3)

    # testing add Exception by hadi
    form = browser.find_element(By.CSS_SELECTOR, ".text-sm .card-title").text
    if form == "Form Resiko":
        resiko()
        gejala()
        login()
    if form == "Form Gejala":
        gejala()
        login()
    else:
        login()

# looping nip dan pass absen
for x in range(len(nip)):
    print("\nloop ke-", x + 1, nip[x][0])
    if nip[x][1] == 0:
        absen(nip[x][0], nip[x][0], nip[x][2])
    else:
        absen(nip[x][0], nip[x][1], nip[x][2])

browser.quit()
print("\nAutomatisasi Absen dengan Web Selenium Python... Selesai")
print('\nsummary : ')   
print(t(tabel, headers="firstrow", tablefmt="psql"))
exit()
