#Jacob Howard 026652585
#Project 2
#October 7th 2019

def main():
    #taking initial input
    savingPerMonth = float(input('How much do you plan to save per month? '))
    yearsSaving = int(input('How many years will you be saving for? '))
    yearsBeforeRaise = int(input('After How many years will you get a raise? '))
    percentageIncrease = float(input('By what percentage would you like to increase your monthly deposit after that amount of time? '))
    accountInterestRate = float(input('What is the account interest rate? '))
    originalDeposit = savingPerMonth

    #print statements to check input
    #print(savingPerMonth)
    #print(yearsSaving)
    #print(yearsBeforeRaise)
    #print(percentageIncrease)

    #initialising variables
    yearCount = 0
    monthCount = 1
    totalMonths = yearsSaving * 12
    internalMonthCount = 1
    monthlyAccountInterestRate = accountInterestRate / 12

    MONTHS_IN_YEAR = 12
    DEPOSIT_INCREASE = 1 + (percentageIncrease/100)
    SAVING_INCREASE = 1 + (monthlyAccountInterestRate/100)

    projectedDeposit = savingPerMonth #amount without interest
    endingDeposit = projectedDeposit * SAVING_INCREASE #amount with interest

    #checking calculation of totalMonths
    #print('Total months  = ' , totalMonths)
    #print('Yearly deposit increase = ' , DEPOSIT_INCREASE)
    #print('interest percentage = ', SAVING_INCREASE)

    print('Year#, Month#, Deposit, ending balance of the month')
    
    while internalMonthCount <= totalMonths:
        print(yearCount,'    ', monthCount,'     ', "{:.2f}".format(projectedDeposit),'  ', "{:.2f}".format(endingDeposit))

        if monthCount % MONTHS_IN_YEAR == 0:
            monthCount = 0
            yearCount += 1

        if yearCount >= 1 and (yearCount % yearsBeforeRaise) == 0:
            if monthCount == 0:
                savingPerMonth = (savingPerMonth * DEPOSIT_INCREASE)
        
        if internalMonthCount < totalMonths:
            projectedDeposit += savingPerMonth
            monthCount += 1
            internalMonthCount += 1
            endingDeposit = (endingDeposit + savingPerMonth) * SAVING_INCREASE
        else:
            monthCount += 1
            internalMonthCount += 1
            
    print('\nIf you deposit $',originalDeposit, 'per month for ',yearsSaving, 'years, and increase the deposit by ',percentageIncrease, '% per year, at bank interest ',accountInterestRate,'%, you will have ', "{:.2f}".format(endingDeposit), 'saved at the end of ', yearsSaving,' years of saving')            

#-----------------------------------PROGRAM START-----------------------------------#       

running = True

main()

while running == True:

    runAgain = int(input('Would you like to use this calculator again? Type 1 for yes or 2 for no\n'))
    if runAgain == 1:
        main()
    else:
        print("Thank you for using this calculator!")
        running = False





    





