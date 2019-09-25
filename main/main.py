import functions

print("""            welcome to tool_management_app              """)

print("""
      choose from following options:
      
      press '1' to add new tool to data base.
      
      press '2' to transfer new tool set to any location.
      
      press '3' to see status of any tool.
      
      """)
option=input()

if option == '1':
    functions.add_new_tool()    
elif option == '2':
    functions.tool_transfer()
elif option == '3':
    functions.tool_status() 
else:
    print('no choice')
    