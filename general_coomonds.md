**Login and Logout**

 az login # Login to Azure account
 az logout # Logout from Azure account

**Set Subscription**

 az account list # List all subscriptions
 az account set --subscription <subscription-id> # Set the active subscription


 **View Resources**

  az resource list            
  az resource show --name <resource-name> --resource-group <resource-group> 


  **Create a Resource Group**
  az group create --name <resource-group-name> --location <location>

  **List Resource Groups**
   az group list 

   **Delete a Resource Group**
 az group delete --name <resource-group-name>

   **Virtual Machines**
    ***Create a Virtual Machine***

    az vm create \
  --resource-group <resource-group-name> \
  --name <vm-name> \
  --image <image-name> \
  --admin-username <username> \
  --admin-password <password>


    *** start/stop the virtual machine***

    az vm start --resource-group <resource-group-name> --name <vm-name>
    az vm stop --resource-group <resource-group-name> --name <vm-name>


  ***Delete a Virtual Machine***
   az vm delete --resource-group <resource-group-name> --name <vm-name>

   **Azure App Services**
   
   ***Create a Web App***
  az webapp create \
  --resource-group <resource-group-name> \
  --plan <app-service-plan-name> \
  --name <webapp-name> \
  --runtime "python|3.9"

   ***delete webapp-service***
   az webapp delete --name <webapp-name> --resource-group <resource-group-name>
  
   **Networking**

   ***Create a Virtual Network (VNet)***

   az network vnet create \
  --name <vnet-name> \
  --resource-group <resource-group-name> \
  --address-prefix <address-prefix>

  ***Create a Subnet***

  az network vnet subnet create \
  --resource-group <resource-group-name> \
  --vnet-name <vnet-name> \
  --name <subnet-name> \
  --address-prefix <address-prefix>




