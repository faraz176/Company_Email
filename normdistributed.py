#Task was to create emails for employees at companies using specified format such as:
# First.Last@company.com or First.Middle.Last@company.com

input = ["https://www.entrust.com/", "http://www.kemps.com", "http://www.westmor-ind.com", 	"http://www.medica.com/default.aspx", "http://www.CambriaUSA.com", "http://brighthealthcare.com"]
input2 = ["James Jones", "Frank Williams", "Jenn Wilson", "Joe Franklin", "Mark F Hamilton", "Sarah M Peterson"]


class NameCompany:

    """ NameCompany Class creates emails for employees and their corresponding company """
    def __init__(self, company_website, employee_name):
        self.finished_company = []
        self.formatted_names = []
        self.completed_email = []
        self.cw = company_website
        self.en = employee_name

    def company_address(self):
        
        #Finding regex pattern to split the company on and extracting the company
        company_names = []
        for i in range(len(self.cw)):
            result = self.cw[i].split("//")
            url = result[1]
            final_comp = url.split('.')
            if final_comp[0] == 'www':
                company_names.append(final_comp[1])
            else:
                company_names.append(final_comp[0])

        #Adding the "@" and ".com" at the end of company names
        
        for i in company_names:
            self.finished_company.append("@" + i +".com")
        
        return self.finished_company

    def employee_name(self):

        #Formating names 
        for i in range(len(self.en)):
            list_of_names = self.en[i].split(" ")
            new_name = ""
            for i in range(len(list_of_names)):
                new_name += "." + list_of_names[i]
            new_name = new_name[1:]
            self.formatted_names.append(new_name)
        return self.formatted_names


    def email_address(self):

        #Zipping names with company
        returned_output = zip(self.formatted_names, self.finished_company)

        #Unpacking the zip and concatenating the name with the company
    
        for i,j in returned_output:
            self.completed_email.append(i + j)

        return self.completed_email


new = NameCompany(input, input2)
new.company_address()
new.employee_name()
print(new.email_address())


        



	
