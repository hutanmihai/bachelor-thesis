import BuyButton from '@/components/BuyButton'
import MaxWidthWrapper from '@/components/max-width-wrapper'
import { TooltipProvider } from '@/components/ui/tooltip'
import { cn } from '@/lib/utils'
import { PRODUCTS } from '@/utils/stripe'

function Pricing() {
  return (
    <MaxWidthWrapper className="mb-8 mt-24 max-w-5xl text-center">
      <div className="mx-auto mb-10 sm:max-w-lg">
        <h1 className="text-6xl font-bold sm:text-7xl">Pricing</h1>
        <p className="mt-5 text-gray-600 sm:text-lg">
          Choose the package that fits your needs. We got you covered.
        </p>
      </div>
      <div className="grid grid-cols-1 gap-10 pt-12">
        <TooltipProvider>
          {PRODUCTS.map((product) => {
            return (
              <div
                key={product.slug}
                className={cn('relative rounded-2xl bg-white shadow-lg', {
                  'border-2 border-primary shadow-blue-200': product.slug === 'five',
                  'border-2 border-purple-600 shadow-purple-200': product.slug === 'ten',
                  'border border-gray-200': product.slug === 'three',
                })}
              >
                {product.slug === 'five' && (
                  <div className="absolute -top-5 left-0 right-0 mx-auto w-32 rounded-full bg-gradient-to-r from-primary to-cyan-600 px-3 py-2 text-sm font-medium text-white">
                    Best seller
                  </div>
                )}
                {product.slug === 'ten' && (
                  <div className="absolute -top-5 left-0 right-0 mx-auto w-32 rounded-full bg-gradient-to-r from-purple-600 to-purple-400 px-3 py-2 text-sm font-medium text-white">
                    Best value
                  </div>
                )}
                <div className="p-5">
                  <h3 className="font-display my-3 text-center text-3xl font-bold">
                    {product.name}
                  </h3>
                  <p className="text-gray-500">
                    {product.pricePerUnit + ' ' + product.currency + ' / ' + 'prediction'}
                  </p>
                  <p className="my-5 text-6xl font-semibold">
                    {product.price + ' ' + product.currency}
                  </p>
                </div>
                <div className="flex h-20 items-center justify-center border-b border-t border-gray-200 bg-gray-50">
                  <div className="flex items-center space-x-1">
                    <p>TODO ADD HERE</p>
                  </div>
                </div>
                <div className="border-t border-gray-200" />
                <div className="p-5">
                  {/* @ts-ignore */}
                  <BuyButton product={product.slug} />
                </div>
              </div>
            )
          })}
        </TooltipProvider>
      </div>
    </MaxWidthWrapper>
  )
}

export default Pricing
