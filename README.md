<!DOCTYPE html>
<html>
<head>
	<title>Wilayah GMIM</title>
</head>
<!-- style css table -->
<style type="text/css" media="all">
table {
    border-collapse: collapse;
}
tbody,
td,
th,
tr {
    border-color: inherit;
    border-style: solid;
    border-width: 3;
}
.table > :not(caption) > * > * {
    padding: 0.3rem 0.6rem;
    color: #80FF00;
}
.table-bordered > :not(caption) > * {
    border-width: 3px 0;
    border-color: #A600FF;
}
.table-bordered > :not(caption) > * > * {
    border-width: 0 3px;
}
</style>
<body>
    <h1>Wilayah GMIM</h1>
    <table class="table table-bordered">
        <thead>
            <tr>
                <th scope="col">No</th>
                <th scope="col">Wilayah</th>
                <th scope="col">Jemaat</th>
                <th scope="col">Kolom</th>
                <th scope="col">Keluarga</th>
                <th scope="col">Anggota</th>
                <th scope="col">Pendeta</th>
                <th scope="col">GA</th>
                <th scope="col">Diaken</th>
                <th scope="col">Penatua</th>
            </tr>
        </thead>
        <tbody id="data-gmim">
        </tbody>
    </table>
	<script>
		// Mengambil data dari file JSON
		fetch('data.json')
		  .then(response => response.json())
		  .then(data => {
		  	// Menampilkan data pada tabel
		    let tableData = '';
		    data.forEach((gmim, index) => {
		      tableData += `            <tr>
                <td>${gmim["No"]}</td>
                <td>${gmim["Nama Wilayah"]}</td>
                <td>${gmim["Jumlah Jemaat"]}</td>
                <td>${gmim["Jumlah Kolom"]}</td>
                <td>${gmim["Jumlah Keluarga"]}</td>
                <td>${gmim["Jumlah Anggota"]}</td>
                <td>${gmim["Jumlah Pendeta"]}</td>
                <td>${gmim["Jumlah GA"]}</td>
                <td>${gmim["Jumlah Diaken"]}</td>
                <td>${gmim["Jumlah Penatua"]}</td>
            </tr>`;
		    });
		    document.getElementById('data-gmim').innerHTML = tableData;
		  })
		  .catch(error => console.error(error));
	</script>
</body>
</html>
