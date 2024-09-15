import { Layout } from 'react-admin'
import {MyAppBar} from './myAppBar'


export const MyLayout = (children: any) => <Layout appBar={MyAppBar}>{children}</Layout>
