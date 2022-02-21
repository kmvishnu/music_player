import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import FavoriteTwoToneIcon from '@mui/icons-material/FavoriteTwoTone';
import { Button } from '@mui/material';




export default function BasicTable(props) {

const songs =props.songs
// const currentSong =props.currentSong
const SetCurrentSong=props.SetCurrentSong
const keyword =props.keyword




  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
      
        <TableBody>
          {songs.filter((val)=>{
            if(keyword===''){return val}
            else if(
              val.name.toLowerCase().includes(keyword.toLowerCase()) ||
              val.author.toLowerCase().includes(keyword.toLowerCase())
            )
            {return val}
          }).map((row,index) => (
           
            <TableRow
              key={index+1}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
             
            >
              
              <TableCell align="right" >
                <Button onClick={()=>SetCurrentSong(row.id)}><img src={row.links.images[0].url} width={60} height={60}/></Button>
              
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
