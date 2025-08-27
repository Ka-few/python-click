from datetime import datetime
import click
from crud import add_tenant, list_tenants, delete_tenant, add_property, list_property, delete_property, add_rental_contract, list_rental_contracts, delete_rental_contract


def main_menu():
    while True:
        click.secho("\n==== Welcome to the Rental Management System ====", fg='green')
        click.secho("1. Manage Tenants", fg='blue')
        click.secho("2. Manage Properties", fg='blue')
        click.secho("3. Manage Rental Contracts", fg='blue')
        click.secho("4. Exit", fg='blue')
        
        user_input = click.prompt("Select Option", type=int)

        if user_input == 1:
            tenants_menu()
        elif user_input == 2:
            property_menu()
        elif user_input == 3:
            rental_contracts_menu()
        elif user_input == 4:
            click.secho("Goodbye!", fg='red')
            break
        else:
            click.secho("Invalid option, try again!", fg='red')


def tenants_menu():
    while True:
        click.secho("\n---- Tenants Menu ----", fg='yellow')
        click.secho("1. Add New Tenant", fg='yellow')
        click.secho("2. List Tenants", fg='yellow')
        click.secho("3. Delete Tenant", fg='yellow')
        click.secho("4. Back to Main Menu", fg='yellow')
        
        tenant_option = click.prompt("Select Tenants Option", type=int)

        if tenant_option == 1:
            click.secho("Adding a new Tenant", fg="green")
            name = click.prompt("Enter Tenant Name")
            gender = click.prompt("Enter Tenant Gender")
            email = click.prompt("Enter Tenant Email")
            try:
                add_tenant(name, gender, email)
                click.secho(f"Tenant {name} added successfully!", fg="green")
            except Exception as e:
                click.secho(f"Error adding Tenant, {e}", fg="red")

        elif tenant_option == 2:
            click.secho("\nTenants List", fg="yellow")
            tenants = list_tenants()
            if tenants:
                for t in tenants:
                    click.secho(f"ID: {t.id} | Name: {t.name} | Gender: {t.gender} | Email: {t.email}", fg="blue")
            else:
                click.secho("No tenants found.", fg="red")

        elif tenant_option == 3:
            tenant_id = click.prompt("Enter Tenant ID to delete", type=int)
            try:
                delete_tenant(tenant_id)
                click.secho(f"Tenant with ID {tenant_id} deleted successfully!", fg="green")
            except Exception as e:
                click.secho(f"Error deleting Tenant, {e}", fg="red")

        elif tenant_option == 4:
            break

        else:
            click.secho("Invalid option, try again!", fg="red")
            
def property_menu():
    while True:
        click.secho("\n---- Properties Menu ----", fg='yellow')
        click.secho("1. Add New Property", fg='yellow')
        click.secho("2. List properties", fg='yellow')
        click.secho("3. Delete property", fg='yellow')
        click.secho("4. Back to Main Menu", fg='yellow')
        
        property_option = click.prompt("Select Properties Option", type=int)

        if property_option == 1:
            click.secho("Adding a new Property", fg="yellow")
            name = click.prompt("Enter Property Name")
            location = click.prompt("Enter property Location")
            house_num = click.prompt("Enter the House number")
            rent_amount = click.prompt("Enter Property Rent Amount")
            try:
                add_property(name, location, house_num, rent_amount)
                click.secho(f"Property {name} added successfully!", fg="green")
            except Exception as e:
                click.secho(f"Error adding property, {e}", fg="red")

        elif property_option == 2:
            click.secho("\nProperty List", fg="yellow")
            properties = list_property()
            if properties:
                for p in properties:
                    click.secho(f"ID: {p.id} | Name: {p.name} | Location: {p.location} | Rent Amount: {p.rent_amount}", fg="blue")
            else:
                click.secho("No properties found.", fg="red")

        elif property_option == 3:
            property_id = click.prompt("Enter Property ID to delete", type=int)
            try:
                delete_tenant(property_id)
                click.secho(f"Property with ID {property_id} deleted successfully!", fg="green")
            except Exception as e:
                click.secho(f"Error deleting Property, {e}", fg="red")

        elif property_option == 4:
            break

        else:
            click.secho("Invalid option, try again!", fg="red")
            

def rental_contracts_menu():
    while True:
        click.secho("\n---- Rental Contracts Menu ----", fg='yellow')
        click.secho("1. Add New Rental Contract", fg='yellow')
        click.secho("2. List Rental Contracts", fg='yellow')
        click.secho("3. Delete Rental Contract", fg='yellow')
        click.secho("4. Back to Main Menu", fg='yellow')
        
        rental_contract_option = click.prompt("Select Rental contract Option", type=int)

        if rental_contract_option == 1:
            click.secho("Adding a new Rental contract", fg="yellow")
            tenant_id = click.prompt("Enter Tenant ID")
            property_id = click.prompt("Enter Property ID")
            start_date = click.prompt("Enter Start date")
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                add_rental_contract(tenant_id, property_id, start_date)
                click.secho(f"Rental contract added successfully!", fg="green")
            except Exception as e:
                click.secho(f"Error adding Rental contract, {e}", fg="red")

        elif rental_contract_option == 2:
            click.secho("\nRental contract List", fg="yellow")
            rental_contracts = list_rental_contracts()
            if rental_contracts:
                for r in rental_contracts:
                    click.secho(f"ID: {r.id} | Tenant ID: {r.tenant_id} | Property ID: {r.property_id} | Start Date: {r.start_date}", fg="blue")
            else:
                click.secho("No Rental contracts found.", fg="red")

        elif rental_contract_option == 3:
            rental_contracts_id = click.prompt("Enter Rental Contract ID to delete", type=int)
            try:
                delete_rental_contract(rental_contracts_id)
                click.secho(f"Rental contract with ID {rental_contracts_id} deleted successfully!", fg="green")
            except Exception as e:
                click.secho(f"Error deleting Rental Contract, {e}", fg="red")

        elif rental_contract_option == 4:
            break

        else:
            click.secho("Invalid option, try again!", fg="red")
            
            


if __name__ == "__main__":
    main_menu()
