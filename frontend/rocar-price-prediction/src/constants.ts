import _ from 'lodash'

export const manufacturerAndModels = {
  bmw: ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7'],
  audi: ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
  mercedes: ['a', 'b', 'c', 'e', 's'],
  dacia: ['logan', 'sandero', 'duster', 'lodgy', 'dokker'],
  fiat: ['500', 'panda', 'punto', 'doblo', 'ducato'],
}

// Function to get all keys from the object
export const getAllManufacturers = () => _.keys(manufacturerAndModels)

// Function to get array for a given key
export const getModelsForManufacturer = (manufacturer: string | undefined) => {
  if (!manufacturer) {
    return []
  }
  return _.get(manufacturerAndModels, manufacturer, [])
}

export const fuelTypes = ['gas', 'diesel', 'hybrid']

export const chassisTypes = ['sedan', 'coupe', 'suv', 'hatchback', 'convertible']

export const gearboxTypes = ['manual', 'automatic']

export const soldByTypes = ['private', 'dealer']
