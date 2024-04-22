type TChipProps = {
  text: string
}

function Chip({ text }: TChipProps) {
  return (
    <div className="flex items-center justify-center rounded-full bg-accent">
      <span className="mx-2 my-1 text-accent-foreground">{text}</span>
    </div>
  )
}

export default Chip
