from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import matplotlib.pyplot as plt
import numpy as np


def main(probs, chan_no):
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get('http://www.site2241.net/erlang.htm')
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "numberChannels"))
    )
    block_probs = []
    for prob in probs:
        driver.find_element(By.NAME, 'offeredLoad').clear()
        driver.find_element(By.NAME, 'offeredLoad').send_keys(prob)

        driver.find_element(By.NAME, 'numberChannels').clear()
        driver.find_element(By.NAME, 'numberChannels').send_keys(chan_no)

        driver.find_element(By.XPATH, "//input[@value='Calculate Blocking Probability']").click()

        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]

        driver.switch_to.window(window_after)
        result = driver.find_element(By.XPATH, "/html/body").text
        driver.close()

        driver.switch_to.window(window_before)
        block_probs.append(round(float(result.split(' ')[-1]), 4))

    print(block_probs)
    print([p - chan_no for p in probs])

    # original formula
    plt.plot([round(x/100, 2) for x in range(0, 100)], [(i - chan_no) for i in probs])

    # simple formula
    plt.plot([round(x / 100, 2) for x in range(0, 100)], [(i - chan_no) / channels ** 2 + 1 / channels for i in probs])

    # simple formula 2
    plt.plot([round(x / 100, 2) for x in range(0, 100)], [(i - chan_no) / channels ** 2 + 2 / channels for i in probs])

    # complex formula
    plt.plot([round(x / 100, 2) for x in range(0, 100)], [(i - chan_no) / channels ** 2 + np.log(chan_no) / channels for i in probs])

    # Vladimir Shakov
    plt.plot([round(x/100, 2) for x in range(0, 100)], [1 - (channels / i) for i in probs])

    # calc
    plt.plot([round(x/100, 2) for x in range(0, 100)], block_probs)
    plt.legend(['ja', 'Shakov', 'kalkulator'])
    plt.xlabel('nadwyżka ruchu  (natężenie [Erl] - liczba kanałów)')
    plt.ylabel('prawdopodobieństow blokady')
    plt.title('liczba kanałów: {}'.format(chan_no))
    plt.savefig('./erlang/chan_{}.png'.format(chan_no), bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    for i in range(1, 11):
        channels = i
        erlang_values = [round(channels + x/100, 2) for x in range(0, 100)]
        print(erlang_values)
        main(erlang_values, channels)
