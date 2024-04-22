import { Card, CardContent, CardFooter, CardHeader } from '@/components/ui/card'

function PredictionsHistory() {
  return [1, 2, 3, 4, 5, 6].map((_, i) => (
    <Card key={i}>
      <CardHeader>Prediction {i}</CardHeader>
      <CardContent>
        <div className="flex justify-between">
          <span>manufacturer: audi</span>
          <span>model: a4</span>
          <span>year: 2023</span>
        </div>
      </CardContent>
      <CardFooter>
        <div>prediction: 5000</div>
      </CardFooter>
    </Card>
  ))
}

export default PredictionsHistory
