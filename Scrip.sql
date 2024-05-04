USE [CI_ControlAccessDb]
GO

/****** Object:  Table [dbo].[New_People]    Script Date: 12/04/2024 2:45:55 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[New_People](
	[Id_User] [int] IDENTITY(1,1) NOT NULL,
	[Email] [nvarchar](50) NULL,
	[UserName] [nvarchar](50) NULL,
	[StoredPassword] [nvarchar](50) NULL
) ON [PRIMARY]
GO


