import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import axios from "axios"
import { useEffect , useState} from "react"
import FavoriteTwoToneIcon from '@mui/icons-material/FavoriteTwoTone';
import { Link } from '@mui/material';




export default function BasicTable() {

  
const [songs,setSongs] = useState([])
const [loading,setLoading] =useState(true)
const [currentSong, setCurrentSong] = useState("")

useEffect(()=>{
    axios.get("http://127.0.0.1:5000/findmusic").then(
        (response)=>{
          setSongs(response.data)
          setLoading(false)
        }).catch(
            error=>console.log(error))}
            ,[])


  const playSong =(x) =>{
    setCurrentSong(x)
  }


  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
      
        <TableBody>
          {songs.map((row) => (
           
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
             
            >
              
              <TableCell align="right" >
              <img src={row.links.images[0].url} width={60} height={60}/>
              </TableCell>
              <TableCell align="left"><b>{row.name}</b><br/>{row.author}</TableCell>
              <TableCell align="left"><FavoriteTwoToneIcon/></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
