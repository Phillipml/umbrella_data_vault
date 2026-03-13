type SearchProps = {
  value: string
  onChange: (value: string) => void
  placeholder?: string
}
export default function Search({
  value,
  onChange,
  placeholder = 'Buscar...'
}: SearchProps) {
  return (
    <input
      type="search"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
    />
  )
}
