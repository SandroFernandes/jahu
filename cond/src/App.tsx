import {
  Admin,
  Resource,
  ListGuesser,
  EditGuesser,
  ShowGuesser,
} from "react-admin";
import { MyLayout } from './myLayout'; 
import { MyAppBar } from './myAppBar';

export const App = () =>  <Admin layout={MyLayout}></Admin> 

