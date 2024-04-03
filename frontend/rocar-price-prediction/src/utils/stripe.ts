import { STRIPE_PUBLIC_KEY } from '@/config.global'
import { loadStripe } from '@stripe/stripe-js'

const stripePromise = loadStripe(STRIPE_PUBLIC_KEY!)

export const PRODUCTS = [
  {
    priceId: process.env.NEXT_PUBLIC_STRIPE_PRICE_ID_TEN,
    name: '10 predictions',
    slug: 'ten',
    price: 80,
    currency: 'ron',
    amount: 10,
    pricePerUnit: 8,
  },
  {
    priceId: process.env.NEXT_PUBLIC_STRIPE_PRICE_ID_FIVE,
    name: '5 predictions',
    slug: 'five',
    price: 45,
    currency: 'ron',
    amount: 5,
    pricePerUnit: 9,
  },
  {
    priceId: process.env.NEXT_PUBLIC_STRIPE_PRICE_ID_THREE,
    name: '3 predictions',
    slug: 'three',
    price: 30,
    currency: 'ron',
    amount: 3,
    pricePerUnit: 10,
  },
]
