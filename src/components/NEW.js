

// import React, { useState, useEffect } from "react";
// export default function Player() {
//   const url =" https://cdn.discordapp.com/attachments/775740994595323954/775741533789224960/Alan_Walker_-_Sing_Me_To_SleepMP3_160K.mp3"
//   const [audio] = useState(new Audio(url));
//   const [playing, setPlaying] = useState(false);
//   const toggle = () => setPlaying(!playing);
//     useEffect(() => {
//         playing ? audio.play() : audio.pause();
//       },
//       [playing]
//     );
//   return (
//     <div>
//       <button onClick={()=>toggle()}>{playing ? "Pause" : "Play"}</button>
//     </div>
//   );
// };

// return (
//   <TableContainer component={Paper}>
//     <Table sx={{ minWidth: 650 }} aria-label="simple table">
    
//       <TableBody>
//         {songs.filter((val)=>{
//           if(keyword==='')
//           {
//             if(allFav.includes(val.id)){
//               return val
//             }
//           }
//           else if(
//             val.name.toLowerCase().includes(keyword.toLowerCase()) ||
//             val.author.toLowerCase().includes(keyword.toLowerCase())
//           )
//           {
//             if(allFav.includes(val.id)){
//               return val
//             }
//           }
          
//         }).map((row,index) => (
         
//           <TableRow
//             key={index+1}
//             sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
           
//           >
            
//             <TableCell align="right" >
//               <Button onClick={()=>SetCurrentSong(row.id)}><img src={row.links.images[0].url} width={60} height={60} alt="artist"/></Button>
            
//             </TableCell>
//             <TableCell align="left"><b>{row.name}</b><br/>{row.author}</TableCell>
//             <TableCell align="left">
//               <Button type="button"  onClick={()=>fav(row.id)}><FavoriteTwoToneIcon/></Button>
//             </TableCell>
//             <TableCell>   
//                 <div>
//                   <Button variant="outlined" onClick={handleClickOpen}>
//                   <AddIcon/>
//                   </Button>
//                   <SimpleDialog
//                     selectedValue={selectedValue}
//                     open={open}
//                     onClose={handleClose}
//                   />
//                 </div>
//             </TableCell>
//           </TableRow>
//         ))}
//       </TableBody>
//     </Table>
//   </TableContainer>
// );
// }