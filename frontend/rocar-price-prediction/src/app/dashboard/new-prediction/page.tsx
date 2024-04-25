import DashboardHeader from '@/components/dashboard-header'
import InferenceForm from '@/components/inference-form'
import MaxWidthWrapper from '@/components/max-width-wrapper'
import { routes } from '@/config.global'

function NewPrediction() {
  return (
    <MaxWidthWrapper className="mb-10 mt-10">
      <DashboardHeader
        linkHref={routes.dashboard.root}
        linkText="See predictions history"
        title="Create new prediction"
      />
      <InferenceForm />
    </MaxWidthWrapper>
  )
}

export default NewPrediction
