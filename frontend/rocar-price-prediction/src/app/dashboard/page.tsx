import DashboardHeader from '@/components/dashboard-header'
import MaxWidthWrapper from '@/components/max-width-wrapper'
import PredictionsHistory from '@/components/predictions-history'
import { routes } from '@/config.global'

function Dashboard() {
  return (
    <MaxWidthWrapper className="mb-10 mt-10">
      <DashboardHeader
        linkHref={routes.dashboard.newPrediction}
        linkText="New prediction"
        title="Predictions history"
      />
      <PredictionsHistory />
    </MaxWidthWrapper>
  )
}

export default Dashboard
