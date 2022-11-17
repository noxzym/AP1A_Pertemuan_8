def Nama_Bulan(bln: int) -> str:
    nama_bln = ""

    match bln:
        case 1:
            nama_bln = "Januari"
        case 2:
            nama_bln = "Februari"
        case 3:
            nama_bln = "Maret"
        case 4:
            nama_bln = "April"
        case 5:
            nama_bln = "Mei"
        case 6:
            nama_bln = "Juni"
        case 7:
            nama_bln = "Juli"
        case 8:
            nama_bln = "Agustus"
        case 9:
            nama_bln = "September"
        case 10:
            nama_bln = "Oktober"
        case 11:
            nama_bln = "November"
        case 12:
            nama_bln = "Desember"

    return nama_bln

tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : "))

nama_bulan = Nama_Bulan(bulan)

print(f"{tanggal} - {nama_bulan} - {tahun}")