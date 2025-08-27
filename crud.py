from models import Tenant, Property, RentalContract, SessionLocal

session = SessionLocal()

def add_tenant(name, gender, email):
    tenant = Tenant(name=name, gender=gender, email=email)
    session.add(tenant)
    session.commit()
    return tenant

def list_tenants():
    return session.query(Tenant).all()

def find_tenant_by_id(tenant_id):
    return session.query(Tenant).filter_by(id=tenant_id).first()

def delete_tenant(tenant_id):
    tenant = find_tenant_by_id(tenant_id)
    if tenant:
        session.delete(tenant)
        session.commit()
        return True
    return False

def add_property(name, location, house_num, rent_amount):
    prop = Property(name=name, location=location, house_num=house_num, rent_amount=rent_amount)
    session.add(prop)
    session.commit()
    return prop

def list_property():
    return session.query(Property).all()

def find_property_by_id(property_id):
    return session.query(Property).filter_by(id=property_id).first()

def delete_property(property_id):
    prop = find_property_by_id(property_id)
    if prop:
        session.delete(prop)
        session.commit()
        return True
    return False

def add_rental_contract(tenant_id, property_id, start_date):
    contract = RentalContract(tenant_id=tenant_id, property_id=property_id, start_date=start_date)
    session.add(contract)
    session.commit()
    return contract

def list_rental_contracts():
    contracts = session.query(RentalContract).all()
    
    for contract in contracts:
        tenant_name = contract.tenant.name if contract.tenant else "Unknown"
        house_num = contract.property.house_num if contract.property else "Unknown"
        print(f"Tenant: {tenant_name}, Property: {house_num}")
    return contracts

def find_contract_by_id(contract_id):
    return session.query(RentalContract).filter_by(id=contract_id).first()

def delete_rental_contract(contract_id):
    contract = find_contract_by_id(contract_id)
    if contract:
        session.delete(contract)
        session.commit()
        return True
    return False