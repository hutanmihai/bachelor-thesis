import _ from 'lodash'

export const selectValues = {
  bmw: ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7'],
  audi: ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
  mercedes: ['a', 'b', 'c', 'e', 's'],
  dacia: ['logan', 'sandero', 'duster', 'lodgy', 'dokker'],
  fiat: ['500', 'panda', 'punto', 'doblo', 'ducato'],
}

// Function to get all keys from the object
export const getAllManufacturers = () => _.keys(selectValues)

// Function to get array for a given key
export const getModelsForManufacturer = (manufacturer: string) =>
  _.get(selectValues, manufacturer, [])
