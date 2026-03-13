type SearchProps = {
  value: string
  onChange: (value: string) => void
  placeholder?: string
  className?: string
}
export default function Search({
  value,
  onChange,
  placeholder = 'Buscar...',
  className
}: SearchProps) {
  return (
    <input
      type="text"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      className={`border-b border-alternative rounded-4xl outline-0 shadow-md shadow-alternative ${className}`}
    />
  )
}
