import os
import pandas as pd
import requests
import ccxt
import datetime
from pycoingecko import CoinGeckoAPI
import ast
import matplotlib.pyplot as plt
import shutil
import webbrowser



print("©Copyright: DiogoSilva2023 + ChatGPT / v1.0")
print("─────────────╔═╗╔═╗───────────────────╔═╗╔═╗─────╔╗──────────────────────")
print("─────────────║║╚╝║║───────────────────║║╚╝║║─────║║──────────────────────")
print("─────────────║╔╗╔╗╠══╦═╗╔══╦╗─╔╗──────║╔╗╔╗╠══╦═╗║║╔╦══╦╗─╔╗─────────────")
print("─────────────║║║║║║╔╗║╔╗╣║═╣║─║║──────║║║║║║╔╗║╔╗╣╚╝╣║═╣║─║║─────────────")
print("─────────────║║║║║║╚╝║║║║║═╣╚═╝║──────║║║║║║╚╝║║║║╔╗╣║═╣╚═╝║─────────────")
print("─────────────╚╝╚╝╚╩══╩╝╚╩══╩═╗╔╝──────╚╝╚╝╚╩══╩╝╚╩╝╚╩══╩═╗╔╝─────────────")
print("───────────────────────────╔═╝║────────────────────────╔═╝║──────────────")
print("───────────────────────────╚══╝────────────────────────╚══╝──────────────")

running = True

if not os.path.exists("coins.csv"):
    with open("coins.csv", "w") as f:
        f.write("coin,balance,description\n")

def main_menu():
    print("--------------------------------------------------------------------------------------------------")
    print("u.   UPDATE MONEY MONKEY")
    print("1.   MODIFY COINS")
    print("2.   INSERT NEW COIN")
    print("3.   ADD BUY + TAX")
    print("v.   VIEW TRACKER")
    print("c.   VIEW COINS")
    print("m.   VIEW METRICS")
    print("g.   GRAPHICS")
    print("s.   ANUAL SAVE")
    print("x.   Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        modify_v1()
    elif choice == "2":
        insert_v1()
    elif choice == "3":
        power_up()
    elif choice == "v":
        opentracker()
    elif choice == "c":
        view_coins()
    elif choice == "g":
        graphs()
    elif choice == "s":
        annual_save()
    elif choice == "m":
        view_metrics()
    elif choice == "u":
        metricsv2()
    elif choice == "x":
        running = False
    else:
        print(" ")
        print("⠀⠀⠀⠀⠀⠀⠀ ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("     ░▓▓          ⠀⠀ ⠀⠀⠀███░⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀░▓   ⠀ ⠀⠀     ░██░   ⠀░▓▓░⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀░▓⠀  ⠀▓▓▓▓⠀⠀⠀⠀ ░██░ ⠀ ⠀░▓▓▓▓░██████⠀")
        print("▓░▓░⠀⠀⠀   ⠀.. .. ⠀⠀⠀   ⠀░▓▓▓▓▓░░░░░▓▓█")
        print("▓░▓▓⠀⠀ ⠀░░░░░░░░░░░      ▓▓▓▓▓▓▓▓▓░░░█")
        print("▓░▓▓⠀⠀ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ⠀███⠀   ░░█")
        print("▓░▓▓⠀⠀░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀  ▓▓██████")
        print("⠀▓▓⠀░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀█░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀█  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░█⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀█▓▓░░..........░░░▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀")
        print("Invalid choice, please try again.")
        print(" ")

def view_metrics():
    try:
        print("------------------------------")
        print("1. AVERAGE")
        print("2. CHANGE")
        print("3. DIFFERENCE")
        print("4. MEDIAN")
        print("m. -MAIN-MENU-")
        mt = input("Chose 1, 2, 3, 4 OR m: ")
        pd.options.display.float_format = '{:.6f}'.format

        if mt == "1":
            if not os.path.exists(f"metrics/averages.csv"):
                print("-----------------------")
                print("---- NO FILE FOUND ----")
                print("-----------------------")
                view_metrics()
            else:
                if os.path.exists(f"metrics/averages.csv"):
                    def color_negative_red(val):
                        color = 'red' if val < 0 else 'green' if val >= 0 else 'black'
                        return 'color: %s' % color
                    df = pd.read_csv("metrics/averages.csv")
                    df = df.style.applymap(color_negative_red)
                    if not os.path.exists(f"metrics/pages"):
                        os.mkdir(f"metrics/pages")
                    df.to_html(f"metrics/pages/averages.html")
                    program_dir = os.path.dirname(os.path.abspath(__file__))
                    filename = os.path.join(program_dir, "metrics/pages/averages.html")
                    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open(filename, new=2)
                    main_menu()

        elif mt == "2":
            if not os.path.exists(f"metrics/changes.csv"):
                print("-----------------------")
                print("---- NO FILE FOUND ----")
                print("-----------------------")
                view_metrics()
            else:
                if os.path.exists(f"metrics/changes.csv"):
                    def color_negative_red(val):
                        color = 'red' if val < 0 else 'green' if val >= 0 else 'black'
                        return 'color: %s' % color
                    df = pd.read_csv("metrics/changes.csv")
                    df = df.style.applymap(color_negative_red)
                    if not os.path.exists(f"metrics/pages"):
                        os.mkdir(f"metrics/pages")
                    df.to_html(f"metrics/pages/changes.html")
                    program_dir = os.path.dirname(os.path.abspath(__file__))
                    filename = os.path.join(program_dir, "metrics/pages/changes.html")
                    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open(filename, new=2)
                    main_menu()

        elif mt == "3":
            if not os.path.exists(f"metrics/differences.csv"):
                print("-----------------------")
                print("---- NO FILE FOUND ----")
                print("-----------------------")
                view_metrics()
            else:
                if os.path.exists(f"metrics/differences.csv"):
                    def color_negative_red(val):
                        color = 'red' if val < 0 else 'green' if val >= 0 else 'black'
                        return 'color: %s' % color
                    df = pd.read_csv("metrics/differences.csv")
                    df = df.style.applymap(color_negative_red)
                    if not os.path.exists(f"metrics/pages"):
                        os.mkdir(f"metrics/pages")
                    df.to_html(f"metrics/pages/differences.html")
                    program_dir = os.path.dirname(os.path.abspath(__file__))
                    filename = os.path.join(program_dir, "metrics/pages/differences.html")
                    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open(filename, new=2)
                    main_menu()

        elif mt == "4":
            if not os.path.exists(f"metrics/medians.csv"):
                print("-----------------------")
                print("---- NO FILE FOUND ----")
                print("-----------------------")
                view_metrics()
            else:
                if os.path.exists(f"metrics/medians.csv"):
                    def color_negative_red(val):
                        color = 'red' if val < 0 else 'green' if val >= 0 else 'black'
                        return 'color: %s' % color
                    df = pd.read_csv("metrics/medians.csv")
                    df = df.style.applymap(color_negative_red)
                    if not os.path.exists(f"metrics/pages"):
                        os.mkdir(f"metrics/pages")
                    df.to_html(f"metrics/pages/medians.html")
                    program_dir = os.path.dirname(os.path.abspath(__file__))
                    filename = os.path.join(program_dir, "metrics/pages/medians.html")
                    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open(filename, new=2)
                    main_menu()
    except:
        print("----------------- CANT DO METRICS ------ MISSING SOME BANANAS -----------------")

def metricsv2():
    merge_and_save()
    try:
        df = pd.read_csv("merged_data.csv")

        if len(df) < 2:
            dfa = "NaN"
        else:
            eur_last_two_values = df['EUR'].tail(2)
            eur_difference = eur_last_two_values.iloc[1] - eur_last_two_values.iloc[0]
            dfa = round(eur_difference, 3)

        if len(df) < 3:
            dfb = "NaN"
        else:
            last_val = df["EUR"].tail(1).values[0]
            last3_value = df["EUR"].tail(3).iloc[-3]
            diff3 = last_val - last3_value
            dfb = round(diff3, 3)

        if len(df) < 4:
            dfc = "NaN"
        else:
            last_val = df["EUR"].tail(1).values[0]
            last4_value = df["EUR"].tail(3).iloc[-3]
            diff4 = last_val - last4_value
            dfc = round(diff4, 3)

        if len(df) < 7:
            dfd = "NaN"
        else:
            last_7_rows = df["EUR"].tail(7)
            median_change7 = last_7_rows.diff().median()
            dfd = round(median_change7, 3)

        if len(df) < 30:
            dfe = "NaN"
        else:
            last_30_rows = df["EUR"].tail(30)
            median_change30 = last_30_rows.diff().median()
            dfe = round(median_change30, 3)

        last_value = df["EUR"].tail(1).values[0]

        if len(df) < 7:
            dff = "NaN"
        else:
            seventh_last_value = df["EUR"].tail(7).iloc[-7]
            difference7 = last_value - seventh_last_value
            dff = round(difference7, 3)

        if len(df) < 14:
            dfg = "NaN"
        else:
            seventh_14_value = df["EUR"].tail(14).iloc[-14]
            difference14 = last_value - seventh_14_value
            dfg = round(difference14, 3)

        if len(df) < 30:
            dfh = "NaN"
        else:
            seventh_30_value = df["EUR"].tail(30).iloc[-30]
            difference30 = last_value - seventh_30_value
            dfh = round(difference30, 3)

        if len(df) < 60:
            dfi = "NaN"
        else:
            seventh_60_value = df["EUR"].tail(60).iloc[-60]
            difference60 = last_value - seventh_60_value
            dfi = round(difference60, 3)

        if len(df) < 21:
            dfj = "NaN"
        else:
            last_21_rows = df["EUR"].tail(21)
            mean_value21 = last_21_rows.mean()
            dfj = round(mean_value21, 3)

        if len(df) < 50:
            dfk = "NaN"
        else:
            last_50_rows = df["EUR"].tail(50)
            mean_value50 = last_50_rows.mean()
            dfk = round(mean_value50, 3)

        if len(df) < 90:
            dfl = "NaN"
        else:
            last_90_rows = df["EUR"].tail(90)
            mean_value90 = last_90_rows.mean()
            dfl = round(mean_value90, 3)

        if len(df) < 200:
            dfm = "NaN"
        else:
            last_200_rows = df["EUR"].tail(200)
            mean_value200 = last_200_rows.mean()
            dfm = round(mean_value200, 3)

        if len(df) < 1:
            last_value = "NaN"
        else:
            last_value = df.at[df.index[-1], 'EUR']
            last_value = round(last_value, 3)

        # frame1 = pd.DataFrame({'EUR': [dfa], 'Diff 3': [dfb], 'Diff 4': [dfc]})
        # frame2 = pd.DataFrame({'median_change7': [dfd], 'median_change30': [dfe]})
        # frame3 = pd.DataFrame({'Change7': [dff], 'Change14': [dfg], 'Change30': [dfh], 'Change60': [dfi]})
        # frame4 = pd.DataFrame(
        #     {'mean21': [dfj], 'mean50': [dfk], 'mean90': [dfl], 'mean200': [dfm], 'value': [last_value]})

        if not os.path.exists("metrics"):
            os.mkdir("metrics")

        try:
            frame1 = pd.read_csv("metrics/differences.csv")
            frame2 = pd.read_csv("metrics/medians.csv")
            frame3 = pd.read_csv("metrics/changes.csv")
            frame4 = pd.read_csv("metrics/averages.csv")
        except FileNotFoundError:
            frame1, frame2, frame3, frame4 = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

        new_frame1 = pd.DataFrame({'EUR': dfa, 'Diff 3': dfb, 'Diff 4': dfc}, index=[0])
        frame1 = pd.concat([frame1, new_frame1])

        new_frame2 = pd.DataFrame({'median_change7': dfd, 'median_change30': dfe}, index=[0])
        frame2 = pd.concat([frame2, new_frame2])

        new_frame3 = pd.DataFrame({'Change7': dff, 'Change14': dfg, 'Change30': dfh, 'Change60': dfi}, index=[0])
        frame3 = pd.concat([frame3, new_frame3])

        new_frame4 = pd.DataFrame(
            {'mean21': dfj, 'mean50': dfk, 'mean90': dfl, 'mean200': dfm, 'value': last_value}, index=[0])
        frame4 = pd.concat([frame4, new_frame4])

        frame1.to_csv(f"metrics/differences.csv", index=False)
        frame2.to_csv(f"metrics/medians.csv", index=False)
        frame3.to_csv(f"metrics/changes.csv", index=False)
        frame4.to_csv(f"metrics/averages.csv", index=False)

    except FileNotFoundError:
        print("values don't exist yet")
        print("-------------------------------------------------------------------------------------------")

    print("/////////////////////////////////////////////////////////////////////")
    print("////////////////////// METRICS HAVE BEEN UPDATED ////////////////////")
    print("/////////////////////////////////////////////////////////////////////")
    main_menu()

def view_coins():
    try:
        pd.options.display.float_format = '{:.6f}'.format
        if os.path.exists("coins.csv"):
            df = pd.read_csv("coins.csv")

            print(" ")
            print("      ▓▓▓▓▓▓▓▓▓▓")
            print("    ▓▓          ▓▓")
            print("  ▓▓    ░░▓░░▓░░░░▓▓")
            print("▓▓    ░░▓▓▓▓▓▓▓▓░░░░▓▓")
            print("▓▓  ░░░░▓▓░░▓▓▓▓░░░░▓▓")
            print("▓▓  ░░░░▓▓░░▓▓░░░░░░▓▓")
            print("▓▓  ░░░░▓▓░░▓▓▓▓░░░░▓▓")
            print("▓▓  ░░░░▓▓▓▓▓▓▓▓░░░░▓▓")
            print("  ▓▓  ░░░░▓░░▓░░░░▓▓")
            print("    ▓▓░░░░░░░░░░▓▓")
            print("      ▓▓▓▓▓▓▓▓▓▓")
            print(" ")



            print("--------------------------------------------------------------")
            print(df)
            print("--------------------------------------------------------------")
        else:
            print(" ")
            print("⠀⠀⠀⠀⠀⠀⠀ ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("     ░▓▓          ⠀⠀ ⠀⠀⠀███░⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀░▓   ⠀ ⠀⠀     ░██░   ⠀░▓▓░⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀░▓⠀  ⠀▓▓▓▓⠀⠀⠀⠀ ░██░ ⠀ ⠀░▓▓▓▓░██████⠀")
            print("▓░▓░⠀⠀⠀   ⠀.. .. ⠀⠀⠀   ⠀░▓▓▓▓▓░░░░░▓▓█")
            print("▓░▓▓⠀⠀ ⠀░░░░░░░░░░░      ▓▓▓▓▓▓▓▓▓░░░█")
            print("▓░▓▓⠀⠀ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ⠀███⠀   ░░█")
            print("▓░▓▓⠀⠀░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀  ▓▓██████")
            print("⠀▓▓⠀░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀█░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀█  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░█⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀█▓▓░░..........░░░▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀")
            print("FILE NOT FOUND!")
            print("--------------------------------------------------------------")
    except:
        print("----------------- CANT DO COINS ------ MISSING SOME BANANAS -----------------")

def modify_v1():
    try:
        pd.options.display.float_format = '{:.6f}'.format
        if os.path.exists("coins.csv"):
            df = pd.read_csv("coins.csv")
            if len(df) < 1:
                print("--------------------------------------------------------------")
                print("YOU CAN´T MODIFY WHAT YOU DONT HAVE. (are you a monkey?)")
                print("--------------------------------------------------------------")
            else:
                print("--------------------------------------------------------------")
                print(df)
                line_to_modify = int(input("Which line would you like to modify? "))
                print(df.iloc[line_to_modify])
                print("--------------------------------------------------------------")
                print("(use SPACE to leave blank!)")
                new_coin = input("What is the new coin name? (Enter to keep the same): ") or df.at[
                    line_to_modify, 'coin']
                print("--------------------------------------------------------------")
                print("(use SPACE to leave blank!)")
                new_balance = input("What is the new balance? (Enter to keep the same): ")
                print("--------------------------------------------------------------")
                if new_balance:
                    try:
                        new_balance = eval(new_balance)
                    except ValueError:
                        print(" ")
                        print("⠀⠀⠀⠀⠀⠀⠀ ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("     ░▓▓          ⠀⠀ ⠀⠀⠀███░⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀░▓   ⠀ ⠀⠀     ░██░   ⠀░▓▓░⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀░▓⠀  ⠀▓▓▓▓⠀⠀⠀⠀ ░██░ ⠀ ⠀░▓▓▓▓░██████⠀")
                        print("▓░▓░⠀⠀⠀   ⠀.. .. ⠀⠀⠀   ⠀░▓▓▓▓▓░░░░░▓▓█")
                        print("▓░▓▓⠀⠀ ⠀░░░░░░░░░░░      ▓▓▓▓▓▓▓▓▓░░░█")
                        print("▓░▓▓⠀⠀ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ⠀███⠀   ░░█")
                        print("▓░▓▓⠀⠀░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀  ▓▓██████")
                        print("⠀▓▓⠀░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀█░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀█  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░█⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀█▓▓░░..........░░░▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("Invalid input for balance")
                        print("--------------------------------------------------------------")
                        return
                else:
                    new_balance = df.at[line_to_modify, 'balance']
                    new_balance = eval(new_balance)
                print("(use space to leave blank!)")
                new_desk = input("What is the new description? (Enter to keep the same): ") or df.at[
                    line_to_modify, 'description']
                df.at[line_to_modify, "coin"] = new_coin
                df.at[line_to_modify, "balance"] = new_balance
                df.at[line_to_modify, "description"] = new_desk
                print("-------------------------UPDATED------------------------------")
                df.to_csv("coins.csv", index=False)
        else:
            newfile = pd.DataFrame(columns=["coin", "balance"])
            newfile.to_csv("coins.csv", index=False)
            print(newfile)
        main_menu()
    except:
        print("----------------- CANT DO MODIFY ------ MISSING SOME BANANAS -----------------")

def insert_v1():
    try:
        pd.options.display.float_format = '{:.6f}'.format
        if os.path.exists("coins.csv"):
            df = pd.read_csv("coins.csv")
            print("--------------------------------------------------------------")
            print("Supported coins ex.: BTC / ETH / LTC")
            print("Unsupported coins ex.: WETH / WMATIC / USDT / USDC")
            print(" ")
            coin = input("---- COIN // as SYMBOL // ")
            print("--------------------------------------------------------------")
            balance = input("---- BALANCE? (you can add multiples with + )")
            balance = eval(balance)
            description = input("---- DESCRIPTION? (y/n): ")
            if description == "y":
                lower = input("WHAT IS THE DESCRIPTION: ")
                new_row = pd.DataFrame([[coin, balance, lower]], columns=["coin", "balance", "description"])
                df = pd.concat([df, new_row], ignore_index=True, verify_integrity=True)
                df.to_csv("coins.csv", index=False)
                print("-------------------------UPDATED------------------------------")
            elif description == "n":
                lower = " "
                new_row = pd.DataFrame([[coin, balance, lower]], columns=["coin", "balance", "description"])
                df = pd.concat([df, new_row], ignore_index=True, verify_integrity=True)
                df.to_csv("coins.csv", index=False)
                print("-------------------------UPDATED------------------------------")
            else:
                print("INVALID KEY, YOU A MONKEY?")
                print("----------------------")
                main_menu()

        else:
            newfile = pd.DataFrame(columns=["coin", "balance", "description"])
            newfile.to_csv("coins.csv", index=False)
            print("----------------------!! UPDATED !!---------------------------")
            print(newfile)
        main_menu()
    except:
        print("----------------- CANT DO INSERT ------ MISSING SOME BANANAS -----------------")

def update_allv2():
    if not os.path.exists("totals"):
        os.mkdir("totals")
    if not os.path.exists("coins.csv"):
        print("NO COINS TO VALUE")
        main_menu()
    else:
        try:
            binance = ccxt.binance()
            print(" ")
            print("////- BINANCE -//// API IS RUNNING, please wait")
            print(" ")
            df = pd.read_csv("coins.csv")
            df["balance"] = df["balance"].astype(float)
            for index, row in df.iterrows():
                ticker = row['coin'] + '/USDT'
                try:
                    market = binance.fetch_ticker(ticker)
                except Exception as e:
                    print(f"!!SHITCOIN!!: {ticker} not found on BINANCE, skipping...")
                    continue
                try:
                    value_usdt = float(market['info']['lastPrice']) * row['balance']
                except:
                    value_usdt = float(market['last']) * row['balance']
                rate = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()['rates']['EUR']
                value_eur = value_usdt * rate
                df.at[index, 'value_usdt'] = value_usdt
                df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_binance.csv", index=False)
            print("--------------------------------------------------------------")
            print("Values calculated and saved to totals_binance.csv")
            print("--------------------------------------------------------------")
        except:
            print("----------------- CANT DO BINANCE ------ MISSING SOME BANANAS -----------------")

        try:
            cryptocom = ccxt.cryptocom()
            print(" ")
            print("////- CRYPTO.COM -//// API IS RUNNING, please wait")
            print(" ")
            df = pd.read_csv("coins.csv")
            df["balance"] = df["balance"].astype(float)
            for index, row in df.iterrows():
                ticker = row['coin'] + '/USDT'
                try:
                    market = cryptocom.fetch_ticker(ticker)
                except Exception as e:
                    print(f"!!SHITCOIN!!: {ticker} not found on CRYPTO.COM, skipping...")
                    continue
                try:
                    value_usdt = float(market['info']['lastPrice']) * row['balance']
                except:
                    value_usdt = float(market['last']) * row['balance']
                rate = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()["rates"]["EUR"]
                value_eur = value_usdt * rate
                df.at[index, 'value_usdt'] = value_usdt
                df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_cryptocom.csv", index=False)
            print("--------------------------------------------------------------")
            print("Values calculated and saved to totals_cryptocom.csv")
            print("--------------------------------------------------------------")
        except:
            print("----------------- CANT DO CRYPTO.COM ------ MISSING SOME BANANAS -----------------")

        try:
            gateio = ccxt.gateio()
            print(" ")
            print("////- GATE.IO -//// API IS RUNNING, please wait")
            print(" ")
            df = pd.read_csv("coins.csv")
            df["balance"] = df["balance"].astype(float)
            for index, row in df.iterrows():
                ticker = row['coin'] + '/USDT'
                try:
                    market = gateio.fetch_ticker(ticker)
                except Exception as e:
                    print(f"!!SHITCOIN!!: {ticker} not found on GATE.IO, skipping...")
                    continue
                try:
                    value_usdt = float(market['info']['lastPrice']) * row['balance']
                except:
                    value_usdt = float(market['last']) * row['balance']
                rate = requests.get(url=f'https://api.exchangerate-api.com/v4/latest/USD').json()['rates']['EUR']
                value_eur = value_usdt * rate
                df.at[index, 'value_usdt'] = value_usdt
                df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_gateio.csv", index=False)
            print("--------------------------------------------------------------")
            print("Values calculated and saved to totals_gateio.csv")
            print("--------------------------------------------------------------")
        except:
            print("----------------- CANT DO GATE.IO ------ MISSING SOME BANANAS -----------------")

        try:
            kraken = ccxt.kraken()
            print(" ")
            print("////- KRAKEN -//// API IS RUNNING, please wait")
            print(" ")
            df = pd.read_csv("coins.csv")
            df["balance"] = df["balance"].astype(float)
            for index, row in df.iterrows():
                ticker = row['coin'] + '/USDT'
                try:
                    market = kraken.fetch_ticker(ticker)
                except Exception as e:
                    print(f"!!SHITCOIN!!: {ticker} not found on KRAKEN, skipping...")
                    continue
                try:
                    value_usdt = float(market['info']['lastPrice']) * row['balance']
                except:
                    value_usdt = float(market['last']) * row['balance']
                rate = requests.get(url=f'https://api.exchangerate-api.com/v4/latest/USD').json()['rates']['EUR']
                value_eur = value_usdt * rate
                df.at[index, 'value_usdt'] = value_usdt
                df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_kraken.csv", index=False)
            print("--------------------------------------------------------------")
            print("Values calculated and saved to totals_kraken.csv")
            print("--------------------------------------------------------------")
        except:
            print("----------------- CANT DO KRAKEN ------ MISSING SOME BANANAS -----------------")

        try:
            coinbasepro = ccxt.coinbasepro()
            print(" ")
            print("////- COINBASE PRO -//// API IS RUNNING, please wait")
            print(" ")
            df = pd.read_csv("coins.csv")
            df["balance"] = df["balance"].astype(float)
            for index, row in df.iterrows():
                ticker = row['coin'] + '/USDT'
                try:
                    market = coinbasepro.fetch_ticker(ticker)
                except Exception as e:
                    print(f"!!SHITCOIN!!: {ticker} not found on COINBASE PRO, skipping...")
                    continue
                try:
                    value_usdt = float(market['info']['lastPrice']) * row['balance']
                except:
                    value_usdt = float(market['last']) * row['balance']
                rate = requests.get(url=f'https://api.exchangerate-api.com/v4/latest/USD').json()['rates']['EUR']
                value_eur = value_usdt * rate
                df.at[index, 'value_usdt'] = value_usdt
                df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_coinbasepro.csv", index=False)
            print("--------------------------------------------------------------")
            print("Values calculated and saved to totals_coinbasepro.csv")
            print("--------------------------------------------------------------")
        except:
            print("----------------- CANT DO COINBASEPRO ------ MISSING SOME BANANAS -----------------")

        try:
            bitfinex = ccxt.bitfinex ()
            print(" ")
            print("////- BITFINEX -//// API IS RUNNING, please wait")
            print(" ")
            df = pd.read_csv("coins.csv")
            df["balance"] = df["balance"].astype(float)
            for index, row in df.iterrows():
                ticker = row['coin'] + '/USDT'
                try:
                    market = bitfinex.fetch_ticker(ticker)
                except Exception as e:
                    print(f"!!SHITCOIN!!: {ticker} not found on BITFINEX, skipping...")
                    continue
                try:
                    value_usdt = float(market['info']['lastPrice']) * row['balance']
                except:
                    value_usdt = float(market['last']) * row['balance']
                rate = requests.get(url=f'https://api.exchangerate-api.com/v4/latest/USD').json()['rates']['EUR']
                value_eur = value_usdt * rate
                df.at[index, 'value_usdt'] = value_usdt
                df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_bitfinex.csv", index=False)
            print("--------------------------------------------------------------")
            print("Values calculated and saved to totals_bitfinex.csv")
            print("--------------------------------------------------------------")
        except:
            print("----------------- CANT DO BITFINEX ------ MISSING SOME BANANAS -----------------")

        try:
            print(" ")
            print("////- COINGECKO -//// API IS RUNNING, please wait")
            print(" ")
            print("note: coingecko doesn´t have SHITCOIN warning")
            print(" ")

            cg = CoinGeckoAPI()
            fuu = pd.read_csv('coins.csv')
            fuu['value_usdt'] = None
            fuu['value_eur'] = None
            for coin in fuu['coin']:
                try:
                    coin_data = cg.get_price(coin, vs_currencies=['usdt', 'eur'])
                    usdt_value = coin_data[coin]['usdt']
                    eur_value = coin_data[coin]['eur']
                    fuu.loc[fuu['coin'] == coin, 'value_usdt'] = usdt_value
                    fuu.loc[fuu['coin'] == coin, 'value_eur'] = eur_value
                except Exception as e:
                    print(f"Searching for {coin}...")
                    continue
            df.to_csv(f"totals/totals_coing", index=False)
            print("--------------------------------------------------------------")
            print("Values calculated and saved to totals_coing.csv")
            print("--------------------------------------------------------------")
        except:
            print("----------------- CANT DO PY.GOINGECKO API ------ MISSING SOME BANANAS -----------------")

    try:
        if os.path.exists(f"totals/totals_binance.csv"):
            df1 = pd.read_csv(f"totals/totals_binance.csv")
            sun = df1[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_binance.csv", index=True, header=True)
        else:
            df = pd.read_csv("coins.csv")
            value_eur = 0
            value_usdt = 0
            df.at[index, 'value_usdt'] = value_usdt
            df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_binance.csv", index=False)
            df1 = pd.read_csv(f"totals/totals_binance.csv")
            sun = df1[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_binance.csv", index=True, header=True)

        if os.path.exists(f"totals/totals_cryptocom.csv"):
            df2 = pd.read_csv(f"totals/totals_cryptocom.csv")
            sun = df2[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_cryptocom.csv", index=True, header=True)
        else:
            df = pd.read_csv("coins.csv")
            value_eur = 0
            value_usdt = 0
            df.at[index, 'value_usdt'] = value_usdt
            df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_cryptocom.csv", index=False)
            df2 = pd.read_csv(f"totals/totals_cryptocom.csv")
            sun = df2[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_cryptocom.csv", index=True, header=True)

        if os.path.exists(f"totals/totals_coing"):
            df3 = pd.read_csv(f"totals/totals_coing")
            sun = df3[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_coing.csv", index=True, header=True)
        else:
            df = pd.read_csv("coins.csv")
            value_eur = 0
            value_usdt = 0
            df.at[index, 'value_usdt'] = value_usdt
            df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_coing", index=False)
            df3 = pd.read_csv(f"totals/totals_coing")
            sun = df3[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_coing.csv", index=True, header=True)

        if os.path.exists(f"totals/totals_gateio.csv"):
            df4 = pd.read_csv(f"totals/totals_gateio.csv")
            sun = df4[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_gateio.csv", index=True, header=True)
        else:
            df = pd.read_csv("coins.csv")
            value_eur = 0
            value_usdt = 0
            df.at[index, 'value_usdt'] = value_usdt
            df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_gateio.csv", index=False)
            df4 = pd.read_csv(f"totals/totals_gateio.csv")
            sun = df4[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_gateio.csv", index=True, header=True)

        if os.path.exists(f"totals/totals_kraken.csv"):
            df5 = pd.read_csv(f"totals/totals_kraken.csv")
            sun = df5[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_kraken.csv", index=True, header=True)
        else:
            df = pd.read_csv("coins.csv")
            value_eur = 0
            value_usdt = 0
            df.at[index, 'value_usdt'] = value_usdt
            df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_kraken.csv", index=False)
            df5 = pd.read_csv(f"totals/totals_kraken.csv")
            sun = df5[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_kraken.csv", index=True, header=True)

        if os.path.exists(f"totals/totals_bitfinex.csv"):
            df6 = pd.read_csv(f"totals/totals_bitfinex.csv")
            sun = df6[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_bitfinex.csv", index=True, header=True)
        else:
            df = pd.read_csv("coins.csv")
            value_eur = 0
            value_usdt = 0
            df.at[index, 'value_usdt'] = value_usdt
            df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_bitfinex.csv", index=False)
            df6 = pd.read_csv(f"totals/totals_bitfinex.csv")
            sun = df6[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_bitfinex.csv", index=True, header=True)

        if os.path.exists(f"totals/totals_coinbasepro.csv"):
            df4 = pd.read_csv(f"totals/totals_coinbasepro.csv")
            sun = df4[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_coinbasepro.csv", index=True, header=True)
        else:
            df = pd.read_csv("coins.csv")
            value_eur = 0
            value_usdt = 0
            df.at[index, 'value_usdt'] = value_usdt
            df.at[index, 'value_eur'] = value_eur
            df.to_csv(f"totals/totals_coinbasepro.csv", index=False)
            df4 = pd.read_csv(f"totals/totals_coinbasepro.csv")
            sun = df4[["value_usdt", "value_eur"]].sum()
            sun.to_csv(f"totals/sums_coinbasepro.csv", index=True, header=True)
    except:
        print("----------------- CANT DO SUMS 1 ------ MISSING SOME BANANAS -----------------")

    try:
        dfa = pd.read_csv(f"totals/sums_binance.csv")
        dfb = pd.read_csv(f"totals/sums_cryptocom.csv")
        dfc = pd.read_csv(f"totals/sums_coing.csv")
        dfd = pd.read_csv(f"totals/sums_gateio.csv")
        dfe = pd.read_csv(f"totals/sums_kraken.csv")
        dff = pd.read_csv(f"totals/sums_coinbasepro.csv")
        dfg = pd.read_csv(f"totals/sums_bitfinex.csv")

        value1 = dfa.loc[1, '0']
        value2 = dfb.loc[1, '0']
        value3 = dfc.loc[1, "0"]
        value4 = dfd.loc[1, "0"]
        value5 = dfe.loc[1, "0"]
        value6 = dff.loc[1, "0"]
        value7 = dfg.loc[1, "0"]
        diff = pd.DataFrame(columns=["value"])
        diff["value"] = [value1, value2, value3, value4, value5, value6, value7]
        print(diff)
        highest_value = diff["value"].max()

        data = {'value': ['value'], 'balance': [highest_value]}
        save = pd.DataFrame(data)
        save.to_csv(f"totals/total_sumsv1.csv", index=False)

        import datetime
        now = datetime.datetime.now()
        current_date = now.strftime("%d-%m-%Y %H:%M:%S")
        if not os.path.exists("tracker"):
            os.mkdir("tracker")
        if not os.path.exists(f"tracker/value_trackerv1.csv"):
            with open(f"tracker/value_trackerv1.csv", "w") as f:
                f.write("date,value\n")
        with open(f"tracker/value_trackerv1.csv", "a") as f:
            f.write(f"{current_date},{highest_value}\n")
        print("--------------------------------------------------------------")
        print("value_trackerv1 SAVED successfully.")
        print("--------------------------------------------------------------")
        print(" ")
        print("/////////////////////////////////////////////////////////////////////")
        print("//////////////// ALL VALUES HAVE BEEN UPDATED ///////////////////////")
        print("/////////////////////////////////////////////////////////////////////")
        profit_loss()
    except:
        print("----------------- CANT DO SUMS 2 ------ MISSING SOME BANANAS -----------------")

def profit_loss():
    try:
        dfaa = pd.read_csv(f"totals/sums_binance.csv")
        dfbb = pd.read_csv(f"totals/sums_cryptocom.csv")
        dfcc = pd.read_csv(f"totals/sums_coing.csv")
        dfdd = pd.read_csv(f"totals/sums_gateio.csv")
        dfee = pd.read_csv(f"totals/sums_kraken.csv")
        dfff = pd.read_csv(f"totals/sums_coinbasepro.csv")
        dfgg = pd.read_csv(f"totals/sums_bitfinex.csv")

        value1 = dfaa.loc[1, '0']
        value2 = dfbb.loc[1, '0']
        value3 = dfcc.loc[1, "0"]
        value4 = dfdd.loc[1, "0"]
        value5 = dfee.loc[1, "0"]
        value6 = dfff.loc[1, "0"]
        value7 = dfgg.loc[1, "0"]
        diff = pd.DataFrame(columns=["value"])
        diff["value"] = [value1, value2, value3, value4, value5, value6, value7]
        highest_value = diff["value"].max()
        print("--------------------------------------------------------------")
        print("Highest value is:")
        print(str(highest_value))
        print("--------------------------------------------------------------")

        own = pd.read_csv("total_tax.csv")
        median = own['0'].median()
        profit_loss = highest_value - median
        print("--------------------------------------------------------------")
        print("PROFIT/LOSS:")
        print(str(profit_loss))
        print("--------------------------------------------------------------")
    except:
        print("----------------- CANT DO PROFIT/LOSS ------ MISSING SOME BANANAS -----------------")

def power_up():
    try:
        if not os.path.exists("Tax.csv"):
            with open("Tax.csv", "w") as f:
                f.write('date', 'reason', 'non_tax', 'taxed')
                df3 = pd.DataFrame(columns=['date', 'reason', 'non_tax', 'taxed'])

        elif os.path.exists("Tax.csv"):
            df3 = pd.read_csv("Tax.csv")

            date = input("Enter the date (DD-MM-YYYY): ")
            reason = input("Enter the reason (ex: BUY BTC): ")
            non_tax = input("Enter the non_taxed amount: ")
            taxed = input("Enter the total amount paid: ")

            new_row = pd.DataFrame({'date': [date], 'reason': [reason], 'non_tax': [non_tax], 'taxed': [taxed]})

            df4 = pd.concat([df3, new_row])

            df4.to_csv("Tax.csv", index=False)
            own1 = df4[["non_tax"]].sum(numeric_only=True)
            own2 = df4[["taxed"]].sum(numeric_only=True)
            fiew = pd.DataFrame({'non_tax': [own1], 'taxed': [own2]})
            fiew.to_csv("total_tax.csv", header=True, index=False)
            print("//////////////// UPDATED TAX + TOTAL TAX ///////////////////////")
            main_menu()
    except:
        print("----------------- CANT DO POWER UP ------ MISSING SOME BANANAS -----------------")

def merge_and_save():
    try:
        df = pd.read_csv("coins.csv")
        if len(df) < 1:
            print(" ")
            print("      ▓▓▓▓▓▓▓▓▓▓")
            print("    ▓▓          ▓▓")
            print("  ▓▓    ░░▓░░▓░░░░▓▓")
            print("▓▓    ░░▓▓▓▓▓▓▓▓░░░░▓▓")
            print("▓▓  ░░░░▓▓░░▓▓▓▓░░░░▓▓")
            print("▓▓  ░░░░▓▓░░▓▓░░░░░░▓▓")
            print("▓▓  ░░░░▓▓░░▓▓▓▓░░░░▓▓")
            print("▓▓  ░░░░▓▓▓▓▓▓▓▓░░░░▓▓")
            print("  ▓▓  ░░░░▓░░▓░░░░▓▓")
            print("    ▓▓░░░░░░░░░░▓▓")
            print("      ▓▓▓▓▓▓▓▓▓▓")
            print(" ")

            print("YOU DONT HAVE COINS YET")
            print("///////////////////////////////////////////////////////////////////////////////")
            main_menu()
        else:

            print("/////////////////////////////////////////////////////////////////////")
            print("/////////////////// MAKING BANANAS HAPPEN ON COINS //////////////////")
            print("/////////////////////////////////////////////////////////////////////")
            update_allv2()
            df2 = pd.read_csv(f"totals/total_sumsv1.csv")
            own = pd.read_csv("total_tax.csv")
            median = own['0'].median()
            eurT = df2.iloc[0, 1]
            profit_loss = eurT - median
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_row = pd.DataFrame({"DATE": [date], "EUR": [eurT], "PROFIT/LOSS": [profit_loss]})
            if not os.path.exists("merged_data.csv"):
                new_file = pd.DataFrame(columns=["DATE", "EUR", "PROFIT/LOSS"])
                new_file.to_csv("merged_data.csv", index=False)

                existing_df = pd.read_csv("merged_data.csv")
                updated_df = pd.concat([existing_df, new_row], ignore_index=True)
                updated_df.to_csv("merged_data.csv", index=False)
                print("////////////////// TRACKER HAS BEEN UPDATED /////////////////////////")

                print("/////////////////////////////////////////////////////////////////////")
                main_menu()
            else:
                existing_df = pd.read_csv("merged_data.csv")
                updated_df = pd.concat([existing_df, new_row], ignore_index=True)
                updated_df.to_csv("merged_data.csv", index=False)
                print("////////////////// TRACKER HAS BEEN UPDATED /////////////////////////")
                print("/////////////////////////////////////////////////////////////////////")
    except:
        print("----------------- CANT DO MERGE_AND_SAVE ------ MISSING SOME BANANAS -----------------")

def opentracker():
    try:
        if os.path.exists("merged_data.csv"):
            df = pd.read_csv("merged_data.csv")

            print("--------------------------------------------------------------")
            print(df.reset_index(drop=True))
            print("--------------------------------------------------------------")
        else:
            print(" ")
            print("⠀⠀⠀⠀⠀⠀⠀ ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("     ░▓▓          ⠀⠀ ⠀⠀⠀███░⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀░▓   ⠀ ⠀⠀     ░██░   ⠀░▓▓░⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀░▓⠀  ⠀▓▓▓▓⠀⠀⠀⠀ ░██░ ⠀ ⠀░▓▓▓▓░██████⠀")
            print("▓░▓░⠀⠀⠀   ⠀.. .. ⠀⠀⠀   ⠀░▓▓▓▓▓░░░░░▓▓█")
            print("▓░▓▓⠀⠀ ⠀░░░░░░░░░░░      ▓▓▓▓▓▓▓▓▓░░░█")
            print("▓░▓▓⠀⠀ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ⠀███⠀   ░░█")
            print("▓░▓▓⠀⠀░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀  ▓▓██████")
            print("⠀▓▓⠀░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀█░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀█  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░█⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀█▓▓░░..........░░░▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀")
            print("File not found")
            print("--------------------------------------------------------------")
        main_menu()
    except:
        print("----------------- CANT DO TRACKER ------ MISSING SOME BANANAS -----------------")

def graphs():
    try:
        print("▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░  ░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░░░░░░░")
        print(" ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒")
        print("██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░  ▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░")
        print(" ▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒░░")
        print(" ██████▓▓██▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░    ▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░")
        print("██████▓▓██▓▓▓▓▓▓░░░░    ░░░░░░  ░░░░  ░░██▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░")
        print(" ██████████▓▓▒▒    ░░▒▒░░░░░░▒▒▒▒██▓▓▒▒░░▒▒████▓▓▓▓▒▒▒▒░░░░░░░░")
        print("██████▓▓████░░░░▒▒████▓▓▓▓▓▓▓▓████▓▓██▓▓▒▒████▓▓▓▓▒▒▒▒░░░░░░░░")
        print(" ████▓▓████▓▓▒▒▓▓██▓▓██████▓▓▓▓██▓▓▒▒▓▓██▓▓████▓▓▓▓▓▓▒▒░░░░")
        print(" ▓▓▓▓▓▓████▓▓▓▓████▓▓██▓▓██▓▓▓▓▓▓██▓▓▓▓▒▒▒▒██████▓▓▓▓░░░░░░░░░░░░░░░░")
        print(" ▓▓████████▓▓██▓▓██▓▓▓▓██▒▒██▒▒▒▒▒▒░░░░░░░░▓▓██▓▓▓▓▒▒░░░░░░░░▒▒▒▒░░░░░░")
        print(" ▓▓██████████▓▓▒▒▒▒░░░░▒▒▒▒▓▓░░▒▒░░░░░░░░░░████▓▓▒▒░░░░░░░░░░▒▒░░░░░░░░")
        print(" ████████████▓▓▒▒▒▒▒▒░░▒▒▒▒░░    ▒▒▓▓▒▒░░▒▒████▓▓░░▒▒▒▒░░░░░░░░░░░░░░░░")
        print(" ████████████▓▓▓▓▓▓▓▓▒▒▒▒░░        ▒▒░░▒▒▓▓████▓▓████▓▓▓▓▒▒░░░░░░░░░░░░")
        print(" ██████████████▓▓▓▓▒▒▒▒░░  ░░        ░░░░▒▒██████████▓▓▓▓▓▓▒▒░░░░░░░░░░")
        print(" ██████████████████▓▓▒▒░░░░▒▒  ░░▒▒    ░░▒▒██████████████████▒▒░░░░░░░░")
        print(" ██████████████▓▓██▓▓░░░░░░▒▒▓▓▒▒  ░░  ░░▒▒████████████████▓▓▓▓▒▒▒▒▒▒▒▒")
        print(" ██████████████▓▓▓▓▓▓░░░░  ░░░░          ▒▒▓▓████████████████▓▓▓▓▓▓▒▒▒▒")
        print(" ████████████████▓▓░░░░░░░░              ▒▒██▓▓██████████████▓▓▒▒▒▒▒▒▒▒")
        print(" ████████████████▓▓▒▒░░░░░░  ░░░░░░░░░░  ▒▒██████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒")
        print(" ██████████████████▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒██████████████▓▓▒▒▒▒▒▒▒▒▒▒▓▓")
        print("██████████████████▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░▓▓██████████████▓▓▒▒▒▒▓▓▓▓████")
        print(" ████████████████████▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓▒▒▓▓████████████████▓▓▓▓████████")
        print(" ████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓██▓▓██████▓▓▓▓▒▒▓▓▓▓██████████")
        print(" ▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓")
        print(" ▓▓▓▓▒▒▓▓▓▓▓▓██████████████▓▓██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print(" ")
        print("////////////////////////////////////////////////////////////////////////")
        print("------- Choose what graphic you want to see")

        print("1. Portfolio value OR profit/loss")
        print("2. Averages + porfolio vlaue")
        print("3. Changes")
        print("4. Medians")
        print("5. COINS % of portfolio")
        print("x. MAIN-MENU")
        print("////////////////////////////////////////////////////////////////////////")
        cho = input("What is you option : ")
        if cho == "1":
            print("1. Portfolio value")
            print("2. Profit/Loss")
            SHAS = input("What is you option : ")
            if not os.path.exists("merged_data.csv"):
                print("YOU CAN SEE THESE BANANAS YET")
                main_menu()
            if SHAS == "1":
                df = pd.read_csv("merged_data.csv")
                plt.plot(df["DATE"], df["EUR"], label="EUR")
                plt.xlabel("DATE")
                plt.ylabel("Values")
                plt.title("Coins' VALUE Over Time")
                plt.legend()
                plt.gca().xaxis.set_tick_params(rotation=90)
                plt.show()
                main_menu()

            if SHAS == "2":
                df = pd.read_csv("merged_data.csv")
                plt.plot(df["DATE"], df["PROFIT/LOSS"], label="PROFIT/LOSS")
                plt.xlabel("DATE")
                plt.ylabel("Values")
                plt.title("Coins' Profit/Loss Over Time")
                plt.legend()
                plt.gca().xaxis.set_tick_params(rotation=90)
                plt.axhline(y=0, color='black', linewidth=1)
                plt.show()
                main_menu()
            else:
                print("Invalid action")
                graphs()

        elif cho == "2":
            if not os.path.exists(f"metrics/averages.csv"):
                print("YOU CAN SEE THESE BANANAS YET")
                main_menu()
            else:
                df = pd.read_csv(f"metrics/averages.csv")
                plt.plot(df['mean21'], 'r', label='mean21')
                plt.plot(df['mean50'], 'g', label='mean50')
                plt.plot(df['mean90'], 'b', label='mean90')
                plt.plot(df['mean200'], 'y', label='mean200')
                plt.plot(df['value'], 'k', label='value')
                plt.xlabel('Index')
                plt.ylabel('Values')
                plt.title('Averages')
                plt.legend()
                plt.show()
                main_menu()

        elif cho == "3":
            if not os.path.exists(f"metrics/changes.csv"):
                print("YOU CAN SEE THESE BANANAS YET")
                main_menu()
            else:
                df = pd.read_csv(f"metrics/changes.csv")
                plt.plot(df['Change7'], 'b', label='Change 7')
                plt.plot(df['Change14'], 'g', label='Change 14')
                plt.plot(df['Change30'], 'c', label='Change 30')
                plt.plot(df['Change60'], 'r', label='Change 60')
                if not os.path.exists(f"metrics/changes.csv"):
                    print("YOU CAN SEE THESE BANANAS YET")
                else:
                    df2 = pd.read_csv(f"metrics/differences.csv")
                    plt.plot(df2['EUR'], 'k', label='Porfolio Value')
                    plt.plot(df2['Diff 3'], 'y', label='Diff 3')
                    plt.plot(df2['Diff 4'], 'm', label='Diff 4')
                    plt.xlabel('Index')
                    plt.ylabel('Values')
                    plt.title('Changes')
                    plt.legend()
                    plt.axhline(y=0, color='black', linewidth=1)
                    plt.show()
                    main_menu()

        elif cho == "4":
            if not os.path.exists(f"metrics/medians.csv"):
                print("YOU CAN SEE THESE BANANAS YET")
                main_menu()
            else:
                df = pd.read_csv(f"metrics/medians.csv")
                plt.plot(df['median_change7'], 'r', label='median change 7')
                plt.plot(df['median_change30'], 'g', label='median change 30')
                plt.xlabel('Index')
                plt.ylabel('Values')
                plt.title('Medians')
                plt.legend()
                plt.show()
                main_menu()

        elif cho == "5":
            print("Insert the name of the -totals- FILE in, -totals- FOLDER, with the most price entries:")
            rah = input("totals_")
            if rah == "binance":
                if not os.path.exists(f"totals/totals_binance.csv"):
                    print("YOU CAN SEE THESE BANANAS YET")
                    main_menu()
                dfdd = pd.read_csv(f"totals/totals_binance.csv")
            elif rah == "cryptocom":
                if not os.path.exists(f"totals/totals_cryptocom.csv"):
                    print("YOU CAN SEE THESE BANANAS YET")
                    main_menu()
                dfdd = pd.read_csv(f"totals/totals_cryptocom.csv")
            elif rah == "kraken":
                if not os.path.exists(f"totals/totals_kraken.csv"):
                    print("YOU CAN SEE THESE BANANAS YET")
                    main_menu()
                dfdd = pd.read_csv(f"totals/totals_kraken.csv")
            elif rah == "bitfinex":
                if not os.path.exists(f"totals/totals_bitfinex.csv"):
                    print("YOU CAN SEE THESE BANANAS YET")
                    main_menu()
                dfdd = pd.read_csv(f"totals/totals_bitfinex.csv")
            elif rah == "coinbasepro":
                if not os.path.exists(f"totals/totals_coinbasepro.csv"):
                    print("YOU CAN SEE THESE BANANAS YET")
                    main_menu()
                dfdd = pd.read_csv(f"totals/totals_coinbasepro.csv")
            elif rah == "coing":
                print("please select another file")
                main_menu()
            elif rah == "gateio":
                if not os.path.exists(f"totals/totals_gateio.csv"):
                    print("YOU CAN SEE THESE BANANAS YET")
                    main_menu()
                dfdd = pd.read_csv(f"totals/totals_gateio.csv")
            else:
                print("INVALID INPUT")

            df = pd.read_csv("coins.csv")
            total_value_eur = dfdd['value_eur'].sum()

            labels = df['coin']
            sizes = dfdd['value_eur'] / total_value_eur

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, radius=1.2,
                    wedgeprops=dict(width=0.5, edgecolor='w'))
            ax1.axis('equal')
            plt.tight_layout()
            plt.show()
            main_menu()
        else:
            print("INVALID INPUT")
    except:
        print("----------------- CANT DO GRAPHICS ------ MISSING SOME BANANAS -----------------")

def annual_save():
    try:
        pd.options.display.float_format = '{:.6f}'.format
        if not os.path.exists("annual_saves"):
            os.makedirs("annual_saves")

        files = os.listdir("annual_saves")

        if not files:
            print("MONKEYS, unfortunately, don't understand symbols")
            print("Please the MONKEYS by choosing a file name as ex.: 01jan2023")
            new_name = input("Enter a new name for GENISYS BANANA file: ")
            shutil.copy("coins.csv", f"annual_saves/{new_name}")
            print(f"copied coins.csv to annual_saves as {new_name}")
            files = os.listdir("annual_saves")

        else:
            df_list = []
            for file in files:
                df = pd.read_csv(f"annual_saves/{file}")
                df['index'] = df.reset_index().index
                df_list.append(df)

            all_df = pd.concat(df_list)

            grouped_df = all_df.groupby(["index", "coin"])["balance"].sum().reset_index()

            final_df = grouped_df.drop(["index"], axis=1)
            final_df["balance"] = pd.to_numeric(final_df["balance"])

            coins_df = pd.read_csv("coins.csv")
            coins_df["balance"] = pd.to_numeric(coins_df["balance"])

            result_df = coins_df.copy()
            result_df["balance"] = coins_df["balance"] - final_df["balance"]

            print("-------------/////////////////-------------/////////////////-------------/////////////////")
            print("----------------------------     TOTAL ANUAL INVESTED  -----------------------------------")
            print("-------------/////////////////-------------/////////////////-------------/////////////////")
            print(result_df)

            save = input("Do you want to save the result? (yes/no)")

            if save.lower() == "yes":
                print("MONKEYS, unfortunately, don't understand symbols")
                print("Please the MONKEYS by choosing a file name as ex.: 01jan2023")
                file_name = input("Enter a file name: ")
                result_df.to_csv(f"annual_saves/{file_name}.csv", index=False)
                print(f"ANUAL BANANAS saved to annual_saves/{file_name}.csv")
            else:
                print("Result not saved.")
    except:
        print("----------------- CANT DO ANUAL_SAVE ------ MISSING SOME BANANAS -----------------")

while running:
    main_menu()
    if "x":
        running = False

if __name__ == "__main__":
    main_menu()
