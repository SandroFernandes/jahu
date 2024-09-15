import AppBar from '@mui/material/AppBar'
import Typography from '@mui/material/Typography'
import Logo from './logo'

export const MyAppBar = () => (
    <AppBar>
        <Logo/>
        <Typography variant="h6" color="inherit" id="react-admin-title">Patrimônio do
            Jahu &nbsp;&nbsp;-&nbsp;&nbsp;</Typography>
        {/* Removed TitlePortal */}
    </AppBar>
);