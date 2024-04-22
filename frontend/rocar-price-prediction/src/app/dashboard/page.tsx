'use client'

import InferenceForm from '@/components/inference-form'
import MaxWidthWrapper from '@/components/max-width-wrapper'
import PredictionsHistory from '@/components/predictions-history'
import { Button } from '@/components/ui/button'
import { useState } from 'react'

function Dashboard() {
  const [isHistoryVisible, setIsHistoryVisible] = useState(true)

  return (
    // TODO
    <MaxWidthWrapper>
      <div className="mt-10 flex w-full gap-10">
        <Button className="w-full" onClick={() => setIsHistoryVisible(true)}>
          See older predictions
        </Button>
        <Button className="w-full" onClick={() => setIsHistoryVisible(false)}>
          Make a new prediction
        </Button>
      </div>
      <div className="mt-10">{isHistoryVisible ? <PredictionsHistory /> : <InferenceForm />}</div>
    </MaxWidthWrapper>
  )
}

export default Dashboard
