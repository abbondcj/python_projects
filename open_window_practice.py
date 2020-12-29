# Opening new windows practice - IDR Desktop Toolkit

from tkinter import *


def use_spread_calculator():
    contract_screen = Tk()
    contract_screen.title("IDR Desktop Toolkit - Spread Calculator")
    contract_screen.geometry("800x400")
    spread_calculator_screen_title = Label(contract_screen, text="Spread Calculator", font="bold")
    spread_calculator_screen_title.pack()

    def contract_button():
        contract_formula_screen = Tk()
        contract_formula_screen.title("Spread Calculator - Contract")
        contract_formula_screen.geometry("800x400")
        contract_screen_title = Label(contract_formula_screen, text="Spread Calculator - Contract", font="bold")
        contract_screen_title.pack()
        pay_rate_entry_label = Label(contract_formula_screen, text="Enter candidate pay rate (XXX.XX)")
        pay_rate_entry_label.pack()
        pay_rate_entry = Entry(contract_formula_screen, width=50, justify=CENTER)
        pay_rate_entry.pack()
        burden_rate_entry_label = Label(contract_formula_screen, text="Enter burden rate (X.XX)")
        burden_rate_entry_label.pack()
        burden_rate_entry = Entry(contract_formula_screen, width=50, justify=CENTER)
        burden_rate_entry.pack()
        bill_rate_entry_label = Label(contract_formula_screen, text="Enter client bill rate (XXX.XX)")
        bill_rate_entry_label.pack()
        bill_rate_entry = Entry(contract_formula_screen, width=50, justify=CENTER)
        bill_rate_entry.pack()
        hours_worked_entry_label = Label(contract_formula_screen, text="Enter hours worked per week (XX.XX)")
        hours_worked_entry_label.pack()
        hours_worked_entry = Entry(contract_formula_screen, width=50, justify=CENTER)
        hours_worked_entry.pack()

        def calculate_spread():
            answers = Label(contract_formula_screen,
                            text="$" + pay_rate_entry.get() + "\t is the entered pay rate \n"
                                 + burden_rate_entry.get() + "\t is the entered burden rate \n"
                                 + "$" + bill_rate_entry.get() + "\t is the entered bill rate \n"
                                 + hours_worked_entry.get() + "\t is the entered hours worked", justify=LEFT)
            answers.pack()
            a = round(float(pay_rate_entry.get()), 3)
            b = round(float(burden_rate_entry.get()), 3)
            c = round(float(bill_rate_entry.get()), 3)
            d = round(float(hours_worked_entry.get()), 3)
            e = round(float(((c - (a * b)) * d)), 3)
            f = format(e, '.2f')
            g = str(f)
            spread = Label(contract_formula_screen, text="$" + g + " is the weekly spread amount", font="bold")
            spread.pack()

        def go_back():
            contract_formula_screen.destroy()

        def quit_program():
            contract_formula_screen.quit()

        calculate_spread_button = Button(contract_formula_screen, text="Click to calculate spread",
                                         command=calculate_spread)
        calculate_spread_button.pack()

        quit_program_button = Button(contract_formula_screen, text="Click to quit program",
                                     command=quit_program)
        quit_program_button.pack(side=BOTTOM)

        go_back_button = Button(contract_formula_screen, text="Click to go back", command=go_back)
        go_back_button.pack(side=BOTTOM)

    def direct_hire_button():
        direct_hire_formula_screen = Tk()
        direct_hire_formula_screen.title("Spread Calculator - Direct Hire")
        direct_hire_formula_screen.geometry("800x400")
        direct_hire_screen_title = Label(direct_hire_formula_screen, text="Spread Calculator - Direct Hire",
                                         font="bold")
        direct_hire_screen_title.pack()
        salary_rate_entry_label = Label(direct_hire_formula_screen, text="Enter candidate DH fee (XXXXX.XX)")
        salary_rate_entry_label.pack()
        salary_rate_entry = Entry(direct_hire_formula_screen, width=50, justify=CENTER)
        salary_rate_entry.pack()
        number_weeks_entry_label = Label(direct_hire_formula_screen, text="Enter the number of weeks to "
                                                                          "spread this fee (XX)")
        number_weeks_entry_label.pack()
        number_weeks_entry = Entry(direct_hire_formula_screen, width=50, justify=CENTER)
        number_weeks_entry.pack()

        def calculate_dh_spread():
            entries = Label(direct_hire_formula_screen, text="$" + salary_rate_entry.get()
                                                             + "\t is the entered DH fee \n"
                                                             + number_weeks_entry.get()
                                                             + "\t is the number of weeks entered",
                            justify=LEFT)
            entries.pack()
            aa = round(float(salary_rate_entry.get()), 3)
            bb = round(float(number_weeks_entry.get()), 3)
            cc = round(float(aa / bb), 3)
            dd = format(cc, '.2f')
            ee = str(dd)
            dh_spread = Label(direct_hire_formula_screen, text="$" + ee + " is the DH fee spread per week",
                              font="bold")
            dh_spread.pack()

        def dh_go_back():
            direct_hire_formula_screen.destroy()

        def dh_quit_program():
            direct_hire_formula_screen.quit()

        calculate_dh_spread_button = Button(direct_hire_formula_screen, text="Click to calculate spread",
                                            command=calculate_dh_spread)
        calculate_dh_spread_button.pack()

        dh_quit_program_button = Button(direct_hire_formula_screen, text="Click to quit program",
                                        command=dh_quit_program)
        dh_quit_program_button.pack(side=BOTTOM)

        dh_go_back_button = Button(direct_hire_formula_screen, text="Click to go back", command=dh_go_back)
        dh_go_back_button.pack(side=BOTTOM)

    def contract_screen_go_back():
        contract_screen.destroy()

    def contract_screen_quit_program():
        contract_screen.quit()

    contract_button = Button(contract_screen, text="Click for contract formula", width=50,
                             pady=50, command=contract_button)
    contract_button.pack()
    direct_hire_button = Button(contract_screen, text="Click for direct hire formula", width=50,
                                pady=50, command=direct_hire_button)
    direct_hire_button.pack()

    contract_screen_quit_program_button = Button(contract_screen, text="Click to quit program",
                                                 command=contract_screen_quit_program)
    contract_screen_quit_program_button.pack(side=BOTTOM)
    contract_screen_go_back_button = Button(contract_screen, text="Click to go back",
                                            command=contract_screen_go_back)
    contract_screen_go_back_button.pack(side=BOTTOM)


def use_pdf_converter():
    pdf_converter_screen = Tk()
    pdf_converter_screen.title("IDR Desktop Toolkit - PDF Converter")
    pdf_converter_screen.geometry("800x400")
    pdf_converter_screen_title = Label(pdf_converter_screen, text="PDF Converter", font="bold")
    pdf_converter_screen_title.pack()


def use_commission_calculator():
    commission_calculator_screen = Tk()
    commission_calculator_screen.title("IDR Desktop Toolkit - Commission Calculator")
    commission_calculator_screen.geometry("800x400")
    commission_calculator_screen_title = Label(commission_calculator_screen, text="Commission Calculator", font="bold")
    commission_calculator_screen_title.pack()

    current_spread_label = Label(commission_calculator_screen, text="Enter your current weekly spread (XXXXX.XX)")
    current_spread_label.pack()
    current_spread_entry = Entry(commission_calculator_screen, width=50, justify=CENTER)
    current_spread_entry.pack()

    def commission_function():
        commission_entry_result = Label(commission_calculator_screen, text="$" + current_spread_entry.get()
                                                                           + "\t is the entered weekly spread",
                                        justify=LEFT)
        commission_entry_result.pack()

        aaa = round(float(current_spread_entry.get()), 3)
        if 1 < aaa <= 1500:
            bbb = aaa * .03
        elif 1500 < aaa <= 3000:
            bbb = aaa * .05
        elif 3000 < aaa <= 5000:
            bbb = aaa * .07
        elif 5000 < aaa <= 10000:
            bbb = aaa * .10
        elif 10000 < aaa <= 15000:
            bbb = aaa * .125
        elif 15000 < aaa <= 20000:
            bbb = aaa * .15
        else:
            bbb = aaa * .20

        ccc = str(round(float(bbb), 3))
        commission_answer = Label(commission_calculator_screen, text="$" + ccc
                                                                     + "\t is your expected weekly commission",
                                  justify=LEFT)
        commission_answer.pack()

    def commission_go_back():
        commission_calculator_screen.destroy()

    def commission_quit_program():
        commission_calculator_screen.quit()

    calculate_commission_button = Button(commission_calculator_screen, text="Click to calculate weekly commission",
                                         command=commission_function)
    calculate_commission_button.pack()
    commission_quit_program_button = Button(commission_calculator_screen, text="Click to quit program",
                                            command=commission_quit_program)
    commission_quit_program_button.pack(side=BOTTOM)
    commission_go_back_button = Button(commission_calculator_screen, text="Click to go back",
                                       command=commission_go_back)
    commission_go_back_button.pack(side=BOTTOM)


# open home screen to program, name window, size window
home_screen = Tk()
home_screen.title("IDR Desktop Toolkit")
home_screen.geometry("800x600")
# add title to home screen and size/add functions to buttons
home_screen_title = Label(text="Welcome to the IDR Desktop Toolkit!", font="bold")
home_screen_title.pack()
spread_calculator_button = Button(text="Click to use Spread Calculator", width=50, pady=50,
                                  command=use_spread_calculator)
spread_calculator_button.pack()
pdf_convert_button = Button(text="Click to use pdf converter", width=50, pady=50,
                            command=use_pdf_converter)
pdf_convert_button.pack()
commission_calculator_button = Button(text="Click to calculate weekly commission", width=50, pady=50,
                                      command=use_commission_calculator)
commission_calculator_button.pack()

home_screen.mainloop()
