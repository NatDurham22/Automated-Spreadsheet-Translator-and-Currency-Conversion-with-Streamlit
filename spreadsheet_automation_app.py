import streamlit as st
import pandas as pd
from deep_translator import GoogleTranslator
from currency_converter import CurrencyConverter

#setting the page title
st.set_page_config(
    page_title='Spreadsheet automation'
)
#reading the template file
df = pd.read_csv('Master_Template_Upload.csv')


st.write('Welcome,')

#instructions for web-app use
st.markdown(
    """Enter the information into the relevant boxes within the form below.
    **once you're sure the data is correct**, click the **'Save Input'** button at the bottom of the form.
    Once the input has been saved, download the csv file by pressing the **'Download as csv'** button located at the bottom of the page"""
)




#create currency converter object
c = CurrencyConverter()


st.title('Spreadsheet automation')

#create function to convert currencies using CurrencyConverter package
def convert_currencies(UK_Price):
    Fr_Price = c.convert(UK_Price,'GBP','EUR')
    Ca_Price = c.convert(UK_Price,'GBP','CAD')
    De_Price = Fr_Price
    Es_Price = Fr_Price
    Ita_Price = Fr_Price
    Jpn_Price = c.convert(UK_Price,'GBP','JPY')
    Mx_Price = c.convert(UK_Price,'GBP','MXN')
    USA_Price = c.convert(UK_Price,'GBP','USD')
    Au_Price = c.convert(UK_Price,'GBP','AUD')#check
    NI_Price = UK_Price #check
    Se_Price = c.convert(UK_Price,'GBP','SEK') #check currency

    #returns a list of the converted prices in Euros, Canadian Dollars, Japanese Yen, US Dollars, Australian dollars and Swedish Krona
    price_list = [Fr_Price,Ca_Price,De_Price,Es_Price,Ita_Price,Jpn_Price,Mx_Price,USA_Price,Au_Price,NI_Price,Se_Price]
    return price_list


#creating a streamlit form for the data-entry
with st.form('dataform'):
    st.write('Input the information into the relevant entries')
#creating input sections for required values and assigning input to original csv file
    #text input boxes are used for fields that require textual information such as product titles and descriptions
    #number input boxes are used for fields that require numeric input such as price and measurements
    #selectboxes are used for fields that have multiple predetermined choices
    SKU = st.text_input('SKU')
    Title = st.text_input('Product Title (ENG)')
    Bin_Rack = st.text_input('Bin Rack')
    Retail_Price = st.number_input('Retail Price (GBP)')
    Purchase_Price = st.number_input('Purchase Price (GBP)')
    Category = st.selectbox('Category',['1','2'])
    Barcode = st.number_input('Barcode')
    Amazon_shipping_template = st.selectbox('Amazon Shipping Template',[])
    Postal_Service = st.selectbox('Postal Service',['1','2'])
    Packaging_Group = st.selectbox('Packaging Group',['1','2'])
    Weight = st.number_input('Weight(mm)')
    Height = st.number_input('Height')
    Width = st.number_input('Width')
    Depth = st.number_input('Depth')
    Tariff_Code = st.number_input('Tariff Code')
    Country_of_Manufacture = st.selectbox('Country of Manufacture',[])
    Suppliers_Name = st.text_input('Suppliers Name')
    DefaultSupplier = st.selectbox('Default Supplier',['1','2'])
    Supplier_Code = st.number_input('Suppliers Code')
    Supplier_Barcode = st.text_input('Supplier Barcode')
    Lead_Time_Days = st.number_input('Lead Time days')
    Supplier_Purchase_Price = st.number_input('Supplier Purchase Price (GBP)')
    Supplier_Min_Order_Qty = st.number_input('Supplier Min Order Qty')
    Supplier_Pack_Size = st.number_input('Supplier Pack Size')
    Location = st.selectbox('Location',['Downstairs','Upstairs'])
    Location_Area = st.selectbox('Location Area',['1','2'])
    Minimum_Level = st.text_input('Minimum Level')
    EBAY0_UK_Price = st.number_input('EBAY0 UK Price')
    EBAY1_UK_Price = st.number_input('EBAY1 UK Price')
    EBAY2_UK_Price = st.number_input('EBAY2 UK Price')
    HS_Shopify = st.number_input('HS Shopify')
    ST_Shopify = st.number_input('ST Shopify')
    UK_Price = st.number_input('UK Price')
    Onbuy_Price = st.number_input('Onbuy Price')
    #data in English
    UK_Title = Title
    USA_Title = Title
    Ca_Title = Title
    Au_Title = Title
    EBAY0_UK_Description = st.text_input('Product Description')
    EBAY1_UK_Description = EBAY0_UK_Description
    EBAY2_UK_Description = EBAY0_UK_Description
    UK_Desc = EBAY0_UK_Description
    USA_Disc = EBAY0_UK_Description
    Ca_Desc = EBAY0_UK_Description
    Au_Desc = EBAY0_UK_Description
    Type = st.text_input('Type')
    Sub_Type = st.text_input('Sub-Type')
    Pack_Size = st.number_input('Pack Size')

    Colour = st.text_input('Colour')
    Size = st.text_input('Size')
    Material = st.selectbox('Material',['Steel','2'])
    Grit_Grade = st.selectbox('Grit Grade',['English Grit Grade','60 Coarse Grit'])
    Finish = st.text_input('Finish')
    Quantity_Size = st.number_input('Quantity/Size')
    Brand = st.text_input('Brand')
    Manufacturer = st.text_input('Manufacturer')

    #product details translated to French
    Fr_Title = GoogleTranslator(source='auto',target='fr').translate(UK_Title)
    Fr_Desc = GoogleTranslator(source='auto',target='fr').translate(UK_Desc)
    EBAY0_Fr_Description = Fr_Desc
    EBAY1_Fr_Description = Fr_Desc
    EBAY2_Fr_Description = Fr_Desc
    Fr_Colour = GoogleTranslator(source='auto',target='fr').translate(Colour)
    Fr_Material = GoogleTranslator(source='auto',target='fr').translate(Material)
    Fr_Grit_Grade = GoogleTranslator(source='auto',target='fr').translate(Grit_Grade)
    Fr_Finish = GoogleTranslator(source='auto',target='fr').translate(Finish)

    #product details translated to German
    De_Title = GoogleTranslator(source='auto',target='de').translate(UK_Title)
    De_Desc = GoogleTranslator(source='auto',target='de').translate(UK_Desc)
    EBAY0_De_Description = De_Desc
    EBAY1_De_Description = De_Desc
    EBAY2_De_Description = De_Desc
    De_Colour = GoogleTranslator(source='auto',target='de').translate(Colour)
    De_Material = GoogleTranslator(source='auto',target='de').translate(Material)
    De_Grit_Grade = GoogleTranslator(source='auto',target='de').translate(Grit_Grade)
    De_Finish = GoogleTranslator(source='auto',target='de').translate(Finish)    
    
    #product details translated to Spanish
    Mx_Title = GoogleTranslator(source='auto',target='es').translate(UK_Title)
    Mx_Desc = GoogleTranslator(source='auto',target='es').translate(UK_Desc)
    Es_Title = Mx_Title
    Es_Desc = Mx_Desc

    Es_Colour = GoogleTranslator(source='auto',target='es').translate(Colour)
    Es_Material = GoogleTranslator(source='auto',target='es').translate(Material)
    Es_Grit_Grade = GoogleTranslator(source='auto',target='es').translate(Grit_Grade)
    Es_Finish = GoogleTranslator(source='auto',target='es').translate(Finish)
    
    #product details translated ton Dutch
    Nl_Title = GoogleTranslator(source='auto',target='nl').translate(UK_Title)
    Nl_Desc = GoogleTranslator(source='auto',target='nl').translate(UK_Desc)
    Nl_Colour = GoogleTranslator(source='auto',target='nl').translate(Colour)
    Nl_Material = GoogleTranslator(source='auto',target='nl').translate(Material)
    Nl_Grit_Grade = GoogleTranslator(source='auto',target='nl').translate(Grit_Grade)
    Nl_Finish = GoogleTranslator(source='auto',target='nl').translate(Finish) 

    #product details translated to Swedish
    Se_Title = GoogleTranslator(source='auto',target='sw').translate(UK_Title)
    Se_Desc = GoogleTranslator(source='auto',target='sw').translate(UK_Desc)
    Se_Colour = GoogleTranslator(source='auto',target='sw').translate(Colour)
    Se_Material = GoogleTranslator(source='auto',target='sw').translate(Material)
    Se_Grit_Grade = GoogleTranslator(source='auto',target='sw').translate(Grit_Grade)
    Se_Finish = GoogleTranslator(source='auto',target='sw').translate(Finish) 
    
    #product details translated to Italian
    It_Title = GoogleTranslator(source='auto',target='it').translate(UK_Title)
    It_Desc = GoogleTranslator(source='auto',target='it').translate(UK_Desc)
    It_Colour = GoogleTranslator(source='auto',target='it').translate(Colour)
    It_Material = GoogleTranslator(source='auto',target='it').translate(Material)
    It_Grit_Grade = GoogleTranslator(source='auto',target='it').translate(Grit_Grade)
    It_Finish = GoogleTranslator(source='auto',target='it').translate(Finish) 

    #product details translated to Japanese
    Jp_Title = GoogleTranslator(source='auto',target='ja').translate(UK_Title)
    Jp_Desc = GoogleTranslator(source='auto',target='ja').translate(UK_Desc)
    Jp_Colour = GoogleTranslator(source='auto',target='ja').translate(Colour)
    Jp_Material = GoogleTranslator(source='auto',target='ja').translate(Material)
    Jp_Grit_Grade = GoogleTranslator(source='auto',target='ja').translate(Grit_Grade)
    Jp_Finish = GoogleTranslator(source='auto',target='ja').translate(Finish) 

    #creating submit button to save the user input
    submitted = st.form_submit_button(label='Save Input')
    
    

    #when submitted, the information will be entered into the reflective field within the template document
    if submitted:
        currencies = convert_currencies(UK_Price)
        #reading the master template csv file and converting to pandas dataframe
        df = pd.read_csv('Master_Template_Upload.csv')

        df['SKU'] = SKU
        df['Title'] = Title
        df['Bin Rack'] = Bin_Rack
        df['Retail Price'] = Retail_Price
        df['Purchase Price'] = Purchase_Price
        df['Category'] = Category
        df['Barcode'] = Barcode
        df['Amazon shipping template'] = Amazon_shipping_template
        df['Postal Service'] = Postal_Service
        df['Weight (mm)'] = Weight
        df['Height'] = Height
        df['Width'] = Width
        df['Depth'] = Depth
        df['Tariff Code'] = Tariff_Code
        df['Country of Manufacture'] = Country_of_Manufacture
        df['Suppliers Name'] = Suppliers_Name
        df['Default Supplier'] = DefaultSupplier
        df['Supplier Code'] = Supplier_Code
        df['Supplier Barcode'] = Supplier_Barcode
        df['Lead Time Days'] = Lead_Time_Days
        df['Supplier Purchase Price'] = Supplier_Purchase_Price
        df['Supplier Min Order Qtt'] = Supplier_Min_Order_Qty
        df['Supplier Pack Size'] = Supplier_Pack_Size
        df['Location'] = Location
        df['Location Area'] = Location_Area
        df['Minimum Level'] = Minimum_Level
        df['EBAY0_UK Price'] = EBAY0_UK_Price
        df['EBAY1_UK Price'] = EBAY1_UK_Price
        df['EBAY2_UK Price'] = EBAY2_UK_Price
        df['HS Shopify'] = HS_Shopify
        df['ST Shopify'] = ST_Shopify
        df['UK Price'] = UK_Price
        df['Fr Price'] = currencies[0]
        df['Ca Price'] = currencies[1]
        df['De Price'] = currencies[2]
        df['Es Price'] = currencies[3]
        df['Ita Price'] = currencies[4]
        df['Jpn Price'] = currencies[5]
        df['Mx Price'] = currencies[6]
        df['USA Price'] = currencies[7]
        df['Au Price'] = currencies[8]
        df['Nl Price'] = currencies[9]
        df['Se Price'] = currencies[10]
        df['Onbuy Price'] = Onbuy_Price
        df['EBAY0_UK Title'] = UK_Title
        df['EBAY1_UK Title'] = UK_Title
        df['EBAY2_UK Title'] = UK_Title
        df['UK Title'] = UK_Title
        df['USA Title'] = USA_Title
        df['Ca Title'] = Ca_Title
        df['Au Title'] = UK_Title
        df['EBAY0_UK Desc'] = EBAY0_UK_Description
        df['EBAY1_UK Desc'] = EBAY1_UK_Description
        df['EBAY2_UK Desc'] = EBAY2_UK_Description
        df['UK Desc'] = UK_Desc
        df['USA Desc'] = USA_Disc
        df['Ca Desc'] = Ca_Desc
        df['Au Desc'] = Au_Desc
        df['Bullet Point 1'] = 1
        df['Bullet Point 2'] = 2
        df['Bullet Point 3'] = 3
        df['Bullet Point 4'] = 4
        df['Bullet Point 5'] = 5
        df['Type.'] = Type
        df['Sub-Type.'] = Sub_Type
        df['Pack Size'] = Pack_Size
        df['Colour'] = Colour
        df['Size'] = Size
        df['Material'] = Material
        df['Grit Grade'] = Grit_Grade
        df['Finish'] = Finish
        df['Quantity / Size'] = Quantity_Size
        df['Brand'] = Brand
        df['Manufacturer'] = Manufacturer
        df['Fr Title'] = Fr_Title
        df['Fr Desc'] = Fr_Desc
        df['Fr Bullet Point 1'] = 1
        df['Fr Bullet Point 2'] = 2
        df['Fr Bullet Point 3'] = 3
        df['Fr Bullet Point 4'] = 4
        df['Fr Bullet Point 5'] = 5
        df['Fr Colour'] = Fr_Colour
        df['Fr Material'] = Fr_Material
        df['Fr Grit Grade'] = Fr_Grit_Grade
        df['Fr Finish'] = Fr_Finish
        df['De Title'] = De_Title
        df['De Desc'] = De_Desc
        df['De Bullet Point 1'] = 1
        df['De Bullet Point 2'] = 2
        df['De Bullet Point 3'] = 3
        df['De Bullet Point 4'] = 4
        df['De Bullet Point 5'] = 5
        df['De Colour'] = De_Colour
        df['De Material'] = De_Material
        df['De Grit Grade'] = De_Grit_Grade
        df['De Finish'] = De_Finish
        df['Mx Title'] = Mx_Title
        df['Es Title'] = Es_Title
        df['Mx Desc'] = Mx_Desc
        df['Es Desc'] = Es_Desc
        df['Es Bullet Point 1'] = 1
        df['Es Bullet Point 2'] = 2
        df['Es Bullet Point 3'] = 3
        df['Es Bullet Point 4'] = 4
        df['Es Bullet Point 5'] = 5
        df['Es Colour'] = Es_Colour
        df['Es Material'] = Es_Material
        df['Es Grit Grade'] = Es_Grit_Grade
        df['Es Finish'] = Es_Finish
        df['Nl Title'] = Nl_Title
        df['Nl Desc'] = Nl_Desc
        df['Nl Bullet Point 1'] = 1
        df['Nl Bullet Point 2'] = 2
        df['Nl Bullet Point 3'] = 3
        df['Nl Bullet Point 4'] = 4
        df['Nl Bullet Point 5'] = 5
        df['Nl Colour'] = Nl_Colour
        df['Nl Material'] = Nl_Material
        df['Nl Grit Grade'] = Nl_Grit_Grade
        df['Nl Finish'] = Nl_Finish
        df['Se Title'] = Se_Title
        df['Se Desc'] = Se_Desc
        df['Se Bullet Point 1'] = 1
        df['Se Bullet Point 2'] = 2
        df['Se Bullet Point 3'] = 3
        df['Se Bullet Point 4'] = 4
        df['Se Bullet Point 5'] = 5
        df['Se Colour'] = Se_Colour
        df['Se Material'] = Se_Material
        df['Se Grit Grade'] = Se_Grit_Grade
        df['Se Finish'] = Se_Finish
        df['It Title'] = It_Title
        df['It Desc'] = It_Desc
        df['It Bullet Point 1'] = 1
        df['It Bullet Point 2'] = 2
        df['It Bullet Point 3'] = 3
        df['It Bullet Point 4'] = 4
        df['It Bullet Point 5'] = 5
        df['It Colour'] = It_Colour
        df['It Material'] = It_Material
        df['It Grit Grade'] = It_Grit_Grade
        df['It Finish'] = It_Finish
        df['Jp Title'] = Jp_Title
        df['Jp Desc'] = Jp_Desc
        df['Jp Bullet Point 1'] = 1
        df['Jp Bullet Point 2'] = 2
        df['Jp Bullet Point 3'] = 3
        df['Jp Bullet Point 4'] = 4
        df['Jp Bullet Point 5'] = 5
        df['Jp Colour'] = Jp_Colour
        df['Jp Material'] = Jp_Material
        df['Jp Grit Grade'] = Jp_Grit_Grade
        df['Jp Finish'] = Jp_Finish
        
        #clearing unnecessary rows from resulting dataframe
        df = df.loc[[0]]
        #displaying the dataframe to allow the user to check the values
        st.dataframe(df)
        
    else:
        st.warning('Please fill in all of the required fields')
#function to convert the dataframe to the required format (csv)        
def convert_df(df):
    return df.to_csv().encode('utf-8')

#calling the csv conversion function
csv = convert_df(df)

#creating a streamlit download button to download the final file
st.download_button(
    label='Download as csv file',
    data=csv,
    file_name='automated_df.csv',
    mime='text/csv',
        )





        
                                    



        
