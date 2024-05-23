import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion'
import { Checkbox } from '@/components/ui/checkbox'
import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { extraOptions, getFieldNameByCategory } from '@/constants'
import { cn } from '@/lib/utils'
import * as React from 'react'
import { useFormContext } from 'react-hook-form'

function ExtraOptions() {
  const form = useFormContext()

  const getSelectedValue = (category: string, values: string[]) => {
    const currentSelectPossibleValues = values
    const currentValues = form.getValues(getFieldNameByCategory(category))
    const presentValues = currentSelectPossibleValues.filter((value) =>
      currentValues.includes(value)
    )
    return presentValues.length ? presentValues[0] : 'Selecteaza'
  }

  return (
    <Accordion type="single" collapsible>
      {Object.entries(extraOptions).map(([category, options], idx) => (
        <AccordionItem key={category} value={`value-${idx}`}>
          <AccordionTrigger>{category}</AccordionTrigger>
          <FormField
            control={form.control}
            name={getFieldNameByCategory(category)}
            render={() => (
              <AccordionContent className="mx-1 grid grid-cols-1 gap-5 md:grid-cols-2">
                {Object.entries(options).map(([option, values]) => (
                  <div key={option} className="flex items-center">
                    {values.length > 0 ? (
                      <FormField
                        control={form.control}
                        name={getFieldNameByCategory(category)}
                        render={({ field, fieldState: { error } }) => (
                          <FormItem className="w-full">
                            <FormLabel className="mb-1">{option}</FormLabel>
                            <FormControl>
                              <Select
                                defaultValue="Selecteaza"
                                value={getSelectedValue(category, values)}
                                disabled={form.formState.isSubmitting}
                                onValueChange={(newValue) => {
                                  const currentSelectPossibleValues = values
                                  const currentValues = form.getValues(
                                    getFieldNameByCategory(category)
                                  )
                                  const presentValues = currentSelectPossibleValues.filter(
                                    (value) => currentValues.includes(value)
                                  )
                                  if (presentValues.length) {
                                    // Remove the older selected value from the array
                                    form.setValue(
                                      getFieldNameByCategory(category),
                                      currentValues.filter(
                                        (value: string) => !presentValues.includes(value)
                                      ),
                                      { shouldValidate: true }
                                    )
                                  } else {
                                    // Add the new item to the array
                                    form.setValue(
                                      getFieldNameByCategory(category),
                                      [...currentValues, newValue],
                                      { shouldValidate: true }
                                    )
                                  }
                                  console.log(form.getValues(getFieldNameByCategory(category)))
                                }}
                              >
                                <FormControl>
                                  <SelectTrigger
                                    className={cn(error ? 'ring-2 ring-destructive' : '')}
                                  >
                                    <SelectValue placeholder="Selecteaza" />
                                  </SelectTrigger>
                                </FormControl>
                                <SelectContent>
                                  <SelectItem value="Selecteaza">Selecteaza</SelectItem>
                                  {values.map((value) => (
                                    <SelectItem key={value} value={value}>
                                      {value}
                                    </SelectItem>
                                  ))}
                                </SelectContent>
                              </Select>
                            </FormControl>
                            {error && (
                              <FormMessage className="mb-0 mt-0.5 line-clamp-1 text-xs">
                                {error.message}
                              </FormMessage>
                            )}
                          </FormItem>
                        )}
                      />
                    ) : (
                      <FormField
                        name={getFieldNameByCategory(category)}
                        control={form.control}
                        render={({ field }) => {
                          return (
                            <FormItem
                              key={option}
                              className="flex flex-row items-start space-x-3 space-y-0"
                            >
                              <FormControl>
                                <div className="flex items-center space-x-2">
                                  <Checkbox
                                    checked={field.value?.includes(option)}
                                    onCheckedChange={(checked) => {
                                      const isChecked = checked
                                        ? field.onChange([...field.value, option])
                                        : field.onChange(
                                            field.value?.filter((value: string) => value !== option)
                                          )
                                      console.log(form.getValues(getFieldNameByCategory(category)))
                                      return isChecked
                                    }}
                                  />
                                  <label
                                    htmlFor={option}
                                    className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                  >
                                    {option}
                                  </label>
                                </div>
                              </FormControl>
                            </FormItem>
                          )
                        }}
                      />
                    )}
                  </div>
                ))}
              </AccordionContent>
            )}
          />
        </AccordionItem>
      ))}
      {/*<AccordionItem value="other-details">*/}
      {/*  <AccordionTrigger>Alte detalii</AccordionTrigger>*/}
      {/*  <AccordionContent className="mx-1 grid grid-cols-1 gap-5 md:grid-cols-2">*/}
      {/*    <RHFInput labelName="Culoare" name="color" placeholder="Introdu culoarea" />*/}
      {/*    <RHFSelect*/}
      {/*      name="color-options"*/}
      {/*      labelName="Optiuni culoare"*/}
      {/*      placeholder="Selecteaza"*/}
      {/*      values={['Standard', 'Metalizata', 'Perlat', 'Mat']}*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Consum urban"*/}
      {/*      name="consumption-urban"*/}
      {/*      placeholder="Introdu consumul urban"*/}
      {/*      type="number"*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Consum extraurban"*/}
      {/*      name="consumption-extraurban"*/}
      {/*      placeholder="Introdu consumul extraurban"*/}
      {/*      type="number"*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Consum mixt"*/}
      {/*      name="consumption-mixt"*/}
      {/*      placeholder="Introdu consumul mixt"*/}
      {/*      type="number"*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Consum mediu"*/}
      {/*      name="consumption-average"*/}
      {/*      placeholder="Introdu consumul mediu"*/}
      {/*      type="number"*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Emisii CO2"*/}
      {/*      name="co2-emissions"*/}
      {/*      placeholder="Introdu emisiile de CO2"*/}
      {/*      type="number"*/}
      {/*    />*/}
      {/*    <RHFSelect*/}
      {/*      name="pollution-norm"*/}
      {/*      labelName="Norma de poluare"*/}
      {/*      placeholder="Selecteaza"*/}
      {/*      values={['Euro 1', 'Euro 2', 'Euro 3', 'Euro 4', 'Euro 5', 'Euro 6', 'Non-Euro']}*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Tara de origine"*/}
      {/*      name="origin-country"*/}
      {/*      placeholder="Introdu tara de origine"*/}
      {/*    />*/}
      {/*    <RHFInput labelName="Versiune" name="version" placeholder="Introdu versiunea" />*/}
      {/*    <RHFInput labelName="Generatie" name="generation" placeholder="Introdu generatia" />*/}
      {/*    <RHFSelect*/}
      {/*      name="transmission"*/}
      {/*      labelName="Transmisie"*/}
      {/*      placeholder="Introdu transmisia"*/}
      {/*      values={['4x4 (manual)', '4x4 (automat)', 'fata', 'spate']}*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Data primei inmatriculari"*/}
      {/*      name="first-registration-date"*/}
      {/*      placeholder="10 decembrie 2021"*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Garantie dealer (inclusa in pret)"*/}
      {/*      name="dealer-warranty-for"*/}
      {/*      placeholder="12 luni"*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Garantie de la producator pana la"*/}
      {/*      name="manufacturer-warranty-until"*/}
      {/*      placeholder="11 noiembrie 2021"*/}
      {/*    />*/}
      {/*    <RHFInput*/}
      {/*      labelName="Sau in limita a"*/}
      {/*      name="manufacturer-warranty-limit"*/}
      {/*      placeholder="100 000 km"*/}
      {/*    />*/}
      {/*    <RHFSwitch labelName="Inmatriculat" name="registered" />*/}
      {/*    <RHFSwitch labelName="Primul proprietar (de nou)" name="first-owner" />*/}
      {/*    <RHFSwitch labelName="Fara accident in istoric" name="no-accident-in-history" />*/}
      {/*    <RHFSwitch labelName="Carte service" name="service-book" />*/}
      {/*  </AccordionContent>*/}
      {/*</AccordionItem>*/}
    </Accordion>
  )
}

export default ExtraOptions
